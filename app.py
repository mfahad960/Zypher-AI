from flask import Flask, jsonify, request
import uuid
import threading
import model

app = Flask(__name__)

# In-memory storage for prediction results
prediction_results = {}

# Route for prediction (supporting async mode)
@app.route("/predict", methods=['POST'])
def predict():
    input_data = "Sample input data for the model"
    
    # Check for the Async-Mode header
    async_mode = request.headers.get('Async-Mode', '').lower() == 'true'
    
    # Generate a unique prediction ID
    prediction_id = str(uuid.uuid4())
    
    if async_mode:
        # If Async-Mode is enabled, process in the background
        prediction_results[prediction_id] = {"status": "processing"}
        
        # Start a background thread to process the task
        threading.Thread(target=process_async_task, args=(prediction_id, input_data)).start()
        
        # Respond immediately with the prediction ID
        return jsonify({
            "message": "Request received. Processing asynchronously.",
            "prediction_id": prediction_id
        }), 202

    else:
        # If Async-Mode is not requested, process synchronously
        result = model.mock_model_predict(input_data)
        return jsonify({"result": result}), 200

def process_async_task(prediction_id, input_data):
    # Process the model prediction (by invoking the the mock function)
    result = model.mock_model_predict(input_data)
    
    # Store the result in the in-memory dictionary
    prediction_results[prediction_id] = {"status": "completed", "output": result}

# Route to retrieve prediction result by prediction_id
@app.route("/predict/<prediction_id>", methods=['GET'])
def get_prediction_result(prediction_id):
    # Check if the prediction ID exists
    result = prediction_results.get(prediction_id)
    
    if not result:
        # If no result found, return 404 Not Found
        return jsonify({"error": "Prediction ID not found."}), 404
    
    if result["status"] == "processing":
        # If the task is still being processed, return 400 Bad Request
        return jsonify({"error": "Prediction is still being processed."}), 400
    
    # If the task is completed, return the result with Code 200
    return jsonify({
        "prediction_id": prediction_id,
        "output": result["output"]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
# this line is for culture