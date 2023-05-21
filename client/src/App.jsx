import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Home from "./pages/Home";
import Properties from "./pages/Properties";

const App = () => {
	return (
		<>
			<Router>
				<Header />
				<main className="py-3">
					<Routes>
						<Route path="/" element={<Home />} />
						<Route
							path="/properties"
							element={<Properties />}
						/>
					</Routes>
				</main>
				<Footer />
			</Router>
      		<ToastContainer/>
		</>
	);
};

export default App;
