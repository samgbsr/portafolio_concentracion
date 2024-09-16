class CreatePredictionResults < ActiveRecord::Migration[7.2]
  def change
    create_table :prediction_results do |t|
      t.text :probabilidades
      t.string :clase_predicha
      t.timestamps
    end
  end
end
