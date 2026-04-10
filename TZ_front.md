5.1. Зона ответственности
Ты отвечаешь за:

React-приложение с 5 экранами
Типизацию всех API-ответов (TypeScript)
Визуализацию графиков (Recharts)
Формы ввода с валидацией
Состояния loading / error / empty
Кнопку «Демо-сценарий» для защиты
Адаптивную верстку
Красивый UX для жюри
5.2. Структура кода
frontend/src/

├── main.tsx                         # Точка входа

├── app/

│   ├── router.tsx                   # React Router: 5 маршрутов

│   └── providers.tsx                # RTK Query provider, Theme

├── components/

│   ├── layout/

│   │   ├── Header.tsx               # Навигация

│   │   ├── Sidebar.tsx              # Боковое меню

│   │   └── PageWrapper.tsx          # Обертка страницы

│   ├── charts/

│   │   ├── IncidentTimeline.tsx     # Линейный график инцидентов

│   │   ├── RegionBarChart.tsx       # Горизонтальный bar по регионам

│   │   ├── ThreatPieChart.tsx       # Круговая диаграмма угроз

│   │   ├── EnterpriseTypeChart.tsx  # Bar по отраслям

│   │   └── ShapWaterfall.tsx        # Waterfall-диаграмма SHAP

│   ├── cards/

│   │   ├── KpiCard.tsx              # Карточка KPI (число + подпись)

│   │   ├── RiskCard.tsx             # Карточка уровня риска (цветная)

│   │   ├── ThreatCard.tsx           # Карточка угрозы

│   │   └── RecommendationCard.tsx   # Карточка рекомендации

│   ├── forms/

│   │   ├── PredictionForm.tsx       # Форма прогноза

│   │   └── FilterPanel.tsx          # Фильтры для дашборда

│   └── common/

│       ├── LoadingSpinner.tsx

│       ├── ErrorMessage.tsx

│       ├── EmptyState.tsx

│       └── Toast.tsx                # Уведомления

├── pages/

│   ├── DashboardPage.tsx            # Экран 1: Обзорная аналитика

│   ├── PredictionPage.tsx           # Экран 2: Прогнозирование

│   ├── VulnerabilityPage.tsx        # Экран 3: Диагностика уязвимостей

│   ├── RecommendationsPage.tsx      # Экран 4: Рекомендации

│   └── ThreatCatalogPage.tsx        # Экран 5: Каталог угроз ФСТЭК

├── services/

│   ├── api.ts                       # Базовый axios/fetch клиент

│   ├── analyticsApi.ts              # Вызовы /analytics/*

│   ├── predictApi.ts                # Вызов /predict

│   ├── threatsApi.ts                # Вызовы /threats

│   ├── recommendationsApi.ts        # Вызовы /recommendations

│   └── scenariosApi.ts              # Вызовы /scenarios/demo

├── types/

│   ├── api.ts                       # Общие типы (Error, Pagination)

│   ├── analytics.ts                 # Типы для аналитики

│   ├── prediction.ts                # Типы для прогноза

│   ├── threat.ts                    # Типы для угроз

│   └── recommendation.ts           # Типы для рекомендаций

├── hooks/

│   ├── useAnalytics.ts

│   ├── usePrediction.ts

│   └── useDemo.ts

├── utils/

│   ├── formatters.ts                # Форматирование чисел, дат

│   ├── riskColors.ts                # Цвета по уровню риска

│   └── constants.ts                 # Константы (URL API, лейблы)

└── assets/

    └── styles/

        └── globals.css
5.3. Экраны — детальное описание
Экран 1: Dashboard (Обзорная аналитика)
┌──────────────────────────────────────────────────────────────┐

│  HEADER: Система прогнозирования киберугроз                   │

├──────────────────────────────────────────────────────────────┤

│                                                               │

│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │

│  │  2000   │ │   943   │ │   187   │ │   89    │            │

│  │Инцидентов│ │Успешных │ │ Угроз   │ │Регионов │            │

│  │  всего  │ │  атак   │ │уникальных│ │         │            │

│  └─────────┘ └─────────┘ └─────────┘ └─────────┘            │

│                                                               │

│  ┌─── Фильтры ──────────────────────────────────────────┐    │

│  │ Регион: [▼ Все]  Отрасль: [▼ Все]  Период: [▼ Год]  │    │

│  └──────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─────────────────────────┐ ┌──────────────────────────┐    │

│  │  Инциденты по месяцам   │ │  Топ-10 регионов         │    │

│  │  (линейный график)      │ │  (горизонтальный bar)    │    │

│  │                         │ │                          │    │

│  │  ~~~~~/\~~~~/\~~~~      │ │  Хабаровский ████████   │    │

│  │  ~~~~/  \~~/  \~~~     │ │  Москва      ███████    │    │

│  │                         │ │  Якутия      ██████     │    │

│  └─────────────────────────┘ └──────────────────────────┘    │

│                                                               │

│  ┌─────────────────────────┐ ┌──────────────────────────┐    │

│  │  Топ-5 угроз            │ │  По отраслям             │    │

│  │  (pie chart)            │ │  (bar chart)             │    │

│  │                         │ │                          │    │

│  │      ╭───╮              │ │  Медицина  ████████████  │    │

│  │    ╭─┤   ├─╮            │ │  НКО       ████████     │    │

│  │    ╰─┤   ├─╯            │ │  Образов.  ██████       │    │

│  │      ╰───╯              │ │                          │    │

│  └─────────────────────────┘ └──────────────────────────┘    │

└──────────────────────────────────────────────────────────────┘

Источники данных:

KPI карточки → GET /api/v1/analytics/summary
График по месяцам → GET /api/v1/analytics/timeseries
Топ регионов → GET /api/v1/analytics/regions
По отраслям → GET /api/v1/analytics/enterprise-types


Экран 2: Prediction (Прогнозирование)
┌──────────────────────────────────────────────────────────────┐

│  ПРОГНОЗИРОВАНИЕ КИБЕРУГРОЗ                                   │

├──────────────────────────────────────────────────────────────┤

│                                                               │

│  ┌─── Форма ввода ──────────────────────────────────────┐    │

│  │                                                       │    │

│  │  Отрасль:    [▼ Медицина        ]                     │    │

│  │  Хосты:      [  1500            ]                     │    │

│  │  Регион:     [▼ Якутия          ]                     │    │

│  │  Дата:       [  2025-05-20      ]                     │    │

│  │                                                       │    │

│  │  [🎯 ДЕМО: Критический]  [🎯 ДЕМО: Средний]          │    │

│  │                                                       │    │

│  │         [ 🔍 АНАЛИЗИРОВАТЬ ]                          │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ═══════════════ РЕЗУЛЬТАТЫ ═══════════════                   │

│                                                               │

│  ┌──────────────────┐  ┌──────────────────┐                  │

│  │  🔴 ВЕРОЯТНОСТЬ   │  │  🕐 ВРЕМЯ АТАКИ  │                  │

│  │     АТАКИ         │  │                  │                  │

│  │    ██████ 85%     │  │  Ночь 00-06      │                  │

│  │  Высокая уверен.  │  │  Пятница         │                  │

│  └──────────────────┘  └──────────────────┘                  │

│                                                               │

│  ┌──────────────────┐  ┌──────────────────┐                  │

│  │  ⚠️ ТИП УГРОЗЫ   │  │  🎯 ОБЪЕКТ       │                  │

│  │                  │  │                  │                  │

│  │  1. УБИ-190 52%  │  │  1. BIOS    62%  │                  │

│  │  2. УБИ-152 19%  │  │  2. Сервер  21%  │                  │

│  │  3. УБИ-163 11%  │  │  3. Сеть     9%  │                  │

│  └──────────────────┘  └──────────────────┘                  │

│                                                               │

│  ┌─── УРОВЕНЬ УЯЗВИМОСТИ ───────────────────────────────┐    │

│  │  🔴 КРИТИЧЕСКИЙ (0.87)                                │    │

│  │  ████████████████████████████░░░░                      │    │

│  │                                                       │    │

│  │  Факторы:                                             │    │

│  │  • Высокая вероятность успешной атаки (85%)           │    │

│  │  • Большое количество хостов (1500)                   │    │

│  │  • Регион с повышенной активностью                    │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── ПОЧЕМУ ТАКОЙ ПРОГНОЗ (SHAP) ─────────────────────┐    │

│  │                                                       │    │

│  │  Отрасль: Медицина        ████████████  +21%          │    │

│  │  Хосты: 1500              █████████     +18%          │    │

│  │  Регион: Якутия           ██████        +12%          │    │

│  │  Сезон: Лето              ████          +8%           │    │

│  │  Сегментация: Низкая      ███           +7%           │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── РЕКОМЕНДАЦИИ ─────────────────────────────────────┐    │

│  │                                                       │    │

│  │  🔴 1. Обновить прошивки BIOS/UEFI                    │    │

│  │     Связано с: УБИ-190                                │    │

│  │                                                       │    │

│  │  🟡 2. Усилить сегментацию сети                       │    │

│  │     Связано с: УБИ-190                                │    │

│  │                                                       │    │

│  │  🟢 3. Усилить ночной мониторинг (00:00-06:00)       │    │

│  │     На основе прогноза времени атаки                  │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── БИЗНЕС-ЦЕННОСТЬ ─────────────────────────────────┐    │

│  │  💰 Потенциальный предотвращенный ущерб: ~15.2 млн ₽ │    │

│  └───────────────────────────────────────────────────────┘    │

└──────────────────────────────────────────────────────────────┘

Источник данных: POST /api/v1/predict

Кнопки ДЕМО: При нажатии заполняют форму предзаготовленными данными из GET /api/v1/scenarios/demo


Экран 3: Vulnerability (Диагностика уязвимостей)
┌──────────────────────────────────────────────────────────────┐

│  ДИАГНОСТИКА УЯЗВИМОСТЕЙ                                      │

├──────────────────────────────────────────────────────────────┤

│                                                               │

│  ┌─── Таблица предприятий ──────────────────────────────┐    │

│  │                                                       │    │

│  │  Код  │ Отрасль    │ Регион     │ Хосты │ Риск       │    │

│  │  ─────┼────────────┼────────────┼───────┼──────────  │    │

│  │  1825 │ Медицина   │ Якутия     │ 1500  │ 🔴 0.87   │    │

│  │  1340 │ НКО        │ Москва     │  120  │ 🟡 0.45   │    │

│  │  2001 │ Образование│ Краснодар  │   45  │ 🟢 0.21   │    │

│  │                                                       │    │

│  │  Сортировка: [▼ По риску ↓]  Фильтр: [▼ Все отрасли] │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── Детали выбранного предприятия ────────────────────┐    │

│  │                                                       │    │

│  │  Предприятие: 1825 (Медицина, Якутия)                │    │

│  │  Всего инцидентов: 12  │  Успешных: 8 (67%)          │    │

│  │  Последний инцидент: 2025-04-15                       │    │

│  │                                                       │    │

│  │  Факторы риска:                                       │    │

│  │  • Высокая доля успешных атак                         │    │

│  │  • Большая поверхность атаки (1500 хостов)           │    │

│  │  • Регион с повышенной активностью                    │    │

│  └───────────────────────────────────────────────────────┘    │

└──────────────────────────────────────────────────────────────┘

Источники данных:

Таблица → GET /api/v1/analytics/summary + данные из enterprise_profiles
Детали → комбинация аналитики и прогноза


Экран 4: Recommendations (Рекомендации)
┌──────────────────────────────────────────────────────────────┐

│  РЕКОМЕНДАЦИИ ПО ЗАЩИТЕ                                       │

├──────────────────────────────────────────────────────────────┤

│                                                               │

│  Фильтры: Угроза [▼ Все]  Уровень [▼ Все]  Объект [▼ Все]  │

│                                                               │

│  ┌─── Приоритет 1 (Критический) ────────────────────────┐    │

│  │  🔴 REC-BIOS-001                                      │    │

│  │  Обновить прошивки BIOS/UEFI на всех хостах           │    │

│  │  Угроза: УБИ-190 │ Объект: BIOS │ Стандарт: ФСТЭК    │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── Приоритет 2 (Высокий) ───────────────────────────┐    │

│  │  🟡 REC-NET-003                                       │    │

│  │  Усилить сегментацию сети                             │    │

│  │  Угроза: УБИ-190 │ Объект: Сеть │ Стандарт: ФСТЭК    │    │

│  └───────────────────────────────────────────────────────┘    │

└──────────────────────────────────────────────────────────────┘

Источник данных: GET /api/v1/recommendations


Экран 5: Threat Catalog (Каталог угроз)
┌──────────────────────────────────────────────────────────────┐

│  КАТАЛОГ УГРОЗ ФСТЭК                                         │

├──────────────────────────────────────────────────────────────┤

│                                                               │

│  Поиск: [  вредоносный код                    ] 🔍           │

│                                                               │

│  ┌─── УБИ-001 ─────────────────────────────────────────┐    │

│  │  Угроза автоматического распространения              │    │

│  │  вредоносного кода в грид-системе                    │    │

│  │                                                       │    │

│  │  Объект: Ресурсные центры грид-системы               │    │

│  │  Нарушения: 🔒К  🔧Ц  ⚡Д                            │    │

│  │  Инцидентов в базе: 12                                │    │

│  │  Статус: Опубликована                                 │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  ┌─── УБИ-002 ─────────────────────────────────────────┐    │

│  │  Угроза агрегирования данных, передаваемых           │    │

│  │  датчиками                                            │    │

│  │  ...                                                  │    │

│  └───────────────────────────────────────────────────────┘    │

│                                                               │

│  Страница: [1] 2 3 4 ... 12                                  │

└──────────────────────────────────────────────────────────────┘

Источник данных: GET /api/v1/threats и GET /api/v1/threats/{ubi_code}
5.4. TypeScript типы (ключевые)
// types/prediction.ts

export interface PredictRequest {

    enterprise_type: EnterpriseType;

    host_count: number;

    region: string;

    observation_date: string;

    additional_context?: {

        internet_exposed?: boolean;

        has_critical_data?: boolean;

        segmentation_level?: 'low' | 'medium' | 'high';

    };

}

export type EnterpriseType =

    | 'Медицина'

    | 'НКО'

    | 'Образование'

    | 'Промышленность'

    | 'Госуправление'

    | 'Финансы'

    | 'Транспорт'

    | 'Энергетика'

    | 'Телеком'

    | 'Другое';

export interface PredictResponse {

    request_id: string;

    model_version: string;

    inference_time_ms: number;

    incident_prediction: IncidentPrediction;

    attack_time_prediction: AttackTimePrediction;

    threat_prediction: ThreatPrediction;

    target_object_prediction: TargetObjectPrediction;

    vulnerability_assessment: VulnerabilityAssessment;

    recommendations: RecommendationItem[];

    explanations: Explanations;

    business_impact: BusinessImpact;

}

export interface IncidentPrediction {

    will_happen: boolean;

    probability: number;

    confidence_level: 'low' | 'medium' | 'high';

    confidence_label: string;

}

export interface AttackTimePrediction {

    time_bucket: 'night' | 'morning' | 'day' | 'evening';

    time_bucket_label: string;

    probable_hour: number;

    probable_day_of_week: string;

    probable_day_label: string;

    probable_season: string;

}

export interface ThreatItem {

    threat_code: string;

    threat_name: string;

    probability: number;

}

export interface ThreatPrediction {

    primary: ThreatItem;

    top_3: ThreatItem[];

}

export interface TargetObjectItem {

    object_code: string;

    object_name: string;

    probability: number;

}

export interface TargetObjectPrediction {

    primary: TargetObjectItem;

    top_3: TargetObjectItem[];

}

export interface VulnerabilityAssessment {

    level: 'low' | 'medium' | 'high' | 'critical';

    level_label: string;

    score: number;

    factors: string[];

}

export interface FeatureExplanation {

    feature: string;

    display_name: string;

    impact: number;

    direction: 'increases_risk' | 'decreases_risk';

    explanation: string;

}

export interface Explanations {

    method: string;

    top_features: FeatureExplanation[];

}

export interface RecommendationItem {

    rec_code: string;

    title: string;

    description: string;

    priority: number;

    priority_label: string;

    related_threat: string | null;

}

export interface BusinessImpact {

    estimated_damage_rub: number;

    damage_label: string;

    calculation_basis?: string;

}

// types/analytics.ts

export interface AnalyticsSummary {

    totals: {

        total_incidents: number;

        successful_incidents: number;

        success_rate: number;

        unique_threats: number;

        unique_regions: number;

        unique_enterprises: number;

        avg_host_count: number;

    };

    top_threats: Array<{

        threat_code: string;

        threat_name: string;

        count: number;

        success_rate: number;

    }>;

    top_regions: Array<{

        region: string;

        count: number;

        success_rate: number;

    }>;

    top_enterprise_types: Array<{

        enterprise_type: string;

        count: number;

        success_rate: number;

    }>;

    filters_applied: Record<string, string | null>;

}

export interface TimeseriesPoint {

    period: string;

    total: number;

    successful: number;

    failed: number;

}

export interface TimeseriesResponse {

    granularity: string;

    series: TimeseriesPoint[];

}
5.5. Цветовая схема рисков
// utils/riskColors.ts

export const RISK_COLORS = {

    critical: { bg: '#FEE2E2', text: '#991B1B', border: '#EF4444', icon: '🔴' },

    high:     { bg: '#FEF3C7', text: '#92400E', border: '#F59E0B', icon: '🟠' },

    medium:   { bg: '#FEF9C3', text: '#854D0E', border: '#EAB308', icon: '🟡' },

    low:      { bg: '#DCFCE7', text: '#166534', border: '#22C55E', icon: '🟢' },

} as const;

export function getRiskColor(level: string) {

    return RISK_COLORS[level as keyof typeof RISK_COLORS]

        ?? RISK_COLORS.medium;

}

export function getRiskLevel(score: number): string {

    if (score >= 0.75) return 'critical';

    if (score >= 0.50) return 'high';

    if (score >= 0.25) return 'medium';

    return 'low';

}
5.6. Порядок работы по часам
Часы 0-4: Скелет
Vite + React + TypeScript + React Router
Layout (Header + Sidebar + PageWrapper)
5 пустых страниц с маршрутами
Базовый API-клиент (axios с baseURL)
Часы 4-12: Dashboard на моках
KPI карточки (компонент KpiCard)
Графики (Recharts: LineChart, BarChart, PieChart)
Фильтры (FilterPanel)
Подключение к mock-endpoints бэкенда
Часы 12-24: Prediction Page
PredictionForm (выпадающие списки, валидация)
Блоки результатов (RiskCard, ThreatCard)
SHAP waterfall (ShapWaterfall)
Рекомендации (RecommendationCard)
Кнопки демо-сценариев
Часы 24-36: Остальные экраны
VulnerabilityPage (таблица + детали)
RecommendationsPage (список + фильтры)
ThreatCatalogPage (поиск + пагинация + карточки)
Часы 36-48: Полировка
Loading/Error/Empty states на всех экранах
Переключение на реальный API
Кнопка «Демо-сценарий» работает в один клик
Адаптивность
Toast-уведомления при ошибках
