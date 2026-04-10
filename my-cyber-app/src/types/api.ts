// Тип для запроса прогноза
export interface PredictRequest {
  enterprise_type: string;
  host_count: number;
  region: string;
}

// Тип для ответа прогноза (основные поля)
export interface PredictResponse {
  request_id: string;
  model_version: string;
  inference_time_ms: number;
  incident_prediction: {
    will_happen: boolean;
    probability: number;
    confidence_level: string;
    confidence_label: string;
  };
  threat_prediction: {
    primary: {
      threat_code: string;
      threat_name: string;
      probability: number;
    };
    top_3: Array<{
      threat_code: string;
      threat_name: string;
      probability: number;
    }>;
  };
  vulnerability_assessment: {
    level: string;
    level_label: string;
    score: number;
    factors: string[];
  };
  business_impact: {
    estimated_damage_rub: number;
    damage_label: string;
  };
  // ... остальные поля по необходимости
}