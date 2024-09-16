require 'httparty'

class PredictionsController < ApplicationController
  protect_from_forgery with: :exception

  def upload
    uploaded_file = params[:file]

    begin
      response = HTTParty.post('http://localhost:5000/predict', body: {
        file: File.open(uploaded_file.path)
      })

      # Check for HTTP status code before proceeding
      if response.success?
        result = response.parsed_response

        if result && result['probabilidades'] && result['clase_predicha']
          PredictionResult.create(
            probabilidades: result['probabilidades'],  # Store as a JSON object or serialize it
            clase_predicha: result['clase_predicha']
          )
        else
          render json: { error: 'Invalid response from prediction service' }, status: 500
          return
        end

        render json: { result: result }
      else
        render json: { error: "Prediction service failed with status: #{response.code}" }, status: 500
      end
    rescue StandardError => e
      render json: { error: "Error during request: #{e.message}" }, status: 500
    end
  end

  def results
    @results = PredictionResult.all.order(created_at: :desc)
  end
end
