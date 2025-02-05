import React from "react";
import Dashboard from "../components/Dashboard";
import ResourceView from "../components/ResourceView";
import RiskAlerts from "../components/RiskAlerts";

const Home = () => {
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Aerospace Project Management</h1>
            <Dashboard />
            <ResourceView />
            <RiskAlerts />
        </div>
    );
};

export default Home;
