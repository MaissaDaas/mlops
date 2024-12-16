import unittest
from src.HousingPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
import numpy as np

class TestPredictionPipeline(unittest.TestCase):

    def test_prediction_pipeline(self):
        # Sample data for testing
        data = CustomData(
            area=100,
            bedrooms=3,
            bathrooms=2,
            stories=2,
            mainroad='yes',
            guestroom='no',
            basement='yes',
            hotwaterheating='yes',
            airconditioning='no',
            parking=2,
            prefarea='yes',
            furnishingstatus='furnished'
        )

        # Convert the data to DataFrame
        final_data = data.get_data_as_dataframe()
        print("Data as DataFrame:")
        print(final_data)

        # Instantiate the PredictPipeline
        predict_pipeline = PredictPipeline()

        # Perform prediction
        prediction = predict_pipeline.predict(final_data)
        print("Prediction Result:")
        print(prediction)

        # Assuming model returns an array of predictions
        self.assertIsInstance(prediction, (list, np.ndarray), "Prediction result should be a list or numpy array.")
        self.assertGreaterEqual(prediction, 0, "Prediction result should not be negative.")
        self.assertIsInstance(prediction[0], (int, float), "The first prediction should be a number.")

        print(f"Predicted value: {round(prediction[0], 2)}")

if __name__ == "__main__":
    unittest.main()
