import { useState } from "react";
import axios from "axios";
import "./index.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [farmer, setFarmer] = useState(null);
  const [parcel, setParcel] = useState(null);
  const [estimate, setEstimate] = useState(null);
  const [listings, setListings] = useState([]);

  const registerFarmer = async () => {
    const res = await axios.post(`${API}/auth/register`, {
      email: "farmer@nuvexa.com",
      password: "123456",
      role: "farmer",
    });
    setFarmer(res.data);
  };

  const addParcel = async () => {
    const res = await axios.post(`${API}/parcels/add`, {
      farmer_id: farmer.id,
      area_hectares: 5,
      crop_type: "rice",
      state: "Karnataka",
      soil_type: "loamy",
      practice_type: "organic",
    });
    setParcel(res.data);
  };

  const generateEstimate = async () => {
    const res = await axios.post(`${API}/estimate/${parcel.id}`);
    setEstimate(res.data);
  };

  const createListing = async () => {
    await axios.post(`${API}/marketplace/create/${estimate.id}`, {
      price_per_tonne: 1200,
    });

    const res = await axios.get(`${API}/marketplace/listings`);
    setListings(res.data);
  };

  return (
    <div className="page">
      <h1>Nuvexa Carbon</h1>
      <p>AI-powered carbon credit marketplace prototype</p>

      <div className="grid">
        <div className="card">
          <h2>1. Farmer Registration</h2>
          <button onClick={registerFarmer}>Register Farmer</button>
          {farmer && <pre>{JSON.stringify(farmer, null, 2)}</pre>}
        </div>

        <div className="card">
          <h2>2. Add Land Parcel</h2>
          <button disabled={!farmer} onClick={addParcel}>
            Add Parcel
          </button>
          {parcel && <pre>{JSON.stringify(parcel, null, 2)}</pre>}
        </div>

        <div className="card">
          <h2>3. Generate Carbon Estimate</h2>
          <button disabled={!parcel} onClick={generateEstimate}>
            Generate Estimate
          </button>
          {estimate && <pre>{JSON.stringify(estimate, null, 2)}</pre>}
        </div>

        <div className="card">
          <h2>4. Create Marketplace Listing</h2>
          <button disabled={!estimate} onClick={createListing}>
            Create Listing
          </button>
        </div>
      </div>

      <div className="card full">
        <h2>Marketplace Listings</h2>
        {listings.length === 0 ? (
          <p>No listings yet.</p>
        ) : (
          listings.map((item) => (
            <div className="listing" key={item.id}>
              <h3>Carbon Credit Listing #{item.id}</h3>
              <p>CO2e: {item.co2e} tonnes</p>
              <p>Trust Score: {item.trust_score}</p>
              <p>Tier: {item.tier}</p>
              <p>Price: ₹{item.price_per_tonne}/tonne</p>
              <p>Status: {item.status}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
