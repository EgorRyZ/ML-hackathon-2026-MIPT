import { BrowserRouter, Routes, Route } from "react-router-dom";

import { DashboardPage } from "../pages/DashboardPage";
import { PredictionPage } from "../pages/PredictionPage";
import { VulnerabilityPage } from "../pages/VulnerabilityPage";
import { RecommendationsPage } from "../pages/RecommendationsPage";
import { ThreatCatalogPage } from "../pages/ThreatCatalogPage";

export const AppRouter = () => {
  return (
    <BrowserRouter>

      <Routes>

        <Route path="/" element={<DashboardPage />} />

        <Route
          path="/prediction"
          element={<PredictionPage />}
        />

        <Route
          path="/vulnerability"
          element={<VulnerabilityPage />}
        />

        <Route
          path="/recommendations"
          element={<RecommendationsPage />}
        />

        <Route
          path="/threats"
          element={<ThreatCatalogPage />}
        />

      </Routes>

    </BrowserRouter>
  );
};