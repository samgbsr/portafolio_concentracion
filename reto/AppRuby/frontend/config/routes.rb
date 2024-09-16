Rails.application.routes.draw do
  # Define the root path
  root 'predictions#index'       # Points the root path ("/") to the PredictionsController's index action

  # Routes for predictions
  post 'upload', to: 'predictions#upload'   # Route for uploading CSV files
  get 'results', to: 'predictions#results'  # Route for showing saved results

  # PWA related routes
  get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker
  get "manifest" => "rails/pwa#manifest", as: :pwa_manifest

  # Health check route
  get "up" => "rails/health#show", as: :rails_health_check
end
