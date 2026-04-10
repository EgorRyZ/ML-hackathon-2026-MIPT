import axios from 'axios';
import { PredictRequest, PredictResponse } from '../types/api';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  timeout: 10000,
});

// Типизированная функция прогноза
export const predict = async (data: PredictRequest): Promise<{ data: PredictResponse }> => {
  // Мок-режим (опционально)
  if (import.meta.env.DEV && !window.location.port.includes('8000')) {
    const mockResponse: PredictResponse = {
      request_id: 'mock-123',
      model_version: 'v1',
      inference_time_ms: 45,
      incident_prediction: {
        will_happen: true,
        probability: 0.87,
        confidence_level: 'high',
        confidence_label: 'Высокая уверенность',
      },
      threat_prediction: {
        primary: {
          threat_code: 'УБИ-190',
          threat_name: 'Вредоносное ПО',
          probability: 0.82,
        },
        top_3: [],
      },
      vulnerability_assessment: {
        level: 'critical',
        level_label: 'КРИТИЧЕСКИЙ',
        score: 0.87,
        factors: ['Большое количество хостов', 'Регион с высокой активностью'],
      },
      business_impact: {
        estimated_damage_rub: 15200000,
        damage_label: '~15.2 млн ₽',
      },
    };
    return { data: mockResponse };
  }

  const response = await api.post<PredictResponse>('/predict', data);
  return response;
};