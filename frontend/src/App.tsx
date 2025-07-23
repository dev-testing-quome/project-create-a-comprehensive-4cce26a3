import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PatientRegistration from './pages/PatientRegistration';
import PatientDashboard from './pages/PatientDashboard';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<PatientRegistration />} />
        <Route path="/dashboard" element={<PatientDashboard />} />
        {/* Add more routes here */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;