// frontend/src/pages/PredictionPage.tsx
import { useState } from 'react';
import PredictionForm from '../components/forms/PredictionForm';
import { usePredictMutation } from '../services/api';
import { PredictRequest, PredictResponse } from '../types/prediction';

export default function PredictionPage() {
  const [predict, { isLoading }] = usePredictMutation();
  const [result, setResult] = useState<PredictResponse | null>(null);

  const handleSubmit = async (formData: PredictRequest) => {
    try {
      const response = await predict(formData).unwrap();
      setResult(response);
    } catch (error) {
      console.error('Prediction failed:', error);
      // Здесь можно добавить Toast-уведомление об ошибке
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Прогнозирование киберугроз</h1>
      <PredictionForm onSubmit={handleSubmit} isLoading={isLoading} />
      {result && (
        <div className="mt-6 p-4 border rounded-lg bg-gray-50">
          <h2 className="text-xl font-semibold mb-2">Результат прогноза</h2>
          <p>
            Вероятность инцидента:{' '}
            <span className="font-mono text-lg">
              {(result.incident_prediction.probability * 100).toFixed(1)}%
            </span>
          </p>
          <p>
            Статус:{' '}
            <span
              className={
                result.incident_prediction.will_happen
                  ? 'text-red-600'
                  : 'text-green-600'
              }
            >
              {result.incident_prediction.will_happen
                ? 'Обнаружена угроза'
                : 'Угроз не выявлено'}
            </span>
          </p>
          <p>
            Уровень уверенности: {result.incident_prediction.confidence_label}
          </p>
          {/* Дополнительные блоки из ТЗ можно добавить позже */}
        </div>
      )}
    </div>
  );
}