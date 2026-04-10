import React, { useState } from 'react';
import { predict } from './api/client';
import { PredictRequest, PredictResponse } from './types/api';

function App() {
  const [form, setForm] = useState<PredictRequest>({
    enterprise_type: 'Медицина',
    host_count: 1500,
    region: 'Москва',
  });
  const [result, setResult] = useState<PredictResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await predict(form);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert('Ошибка при получении прогноза');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>🔐 Прогнозирование киберугроз</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Отрасль:</label>
          <select
            value={form.enterprise_type}
            onChange={e => setForm({ ...form, enterprise_type: e.target.value })}
          >
            <option>Медицина</option>
            <option>НКО</option>
            <option>Образование</option>
          </select>
        </div>
        <div>
          <label>Количество хостов:</label>
          <input
            type="number"
            value={form.host_count}
            onChange={e => setForm({ ...form, host_count: Number(e.target.value) })}
          />
        </div>
        <div>
          <label>Регион:</label>
          <input
            value={form.region}
            onChange={e => setForm({ ...form, region: e.target.value })}
          />
        </div>
        <button type="submit" disabled={loading}>Получить прогноз</button>
      </form>

      {loading && <div>Загрузка...</div>}
      {result && (
        <div style={{ marginTop: '2rem', background: '#f0f0f0', padding: '1rem' }}>
          <h3>Результат прогноза</h3>
          <p>Вероятность инцидента: {(result.incident_prediction.probability * 100).toFixed(1)}%</p>
          <p>Основная угроза: {result.threat_prediction.primary.threat_name}</p>
          <p>Уровень уязвимости: {result.vulnerability_assessment.level_label}</p>
          <p>Предотвращённый ущерб: {result.business_impact.damage_label}</p>
        </div>
      )}
    </div>
  );
}

export default App;