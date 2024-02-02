// Import necessary dependencies
import React from 'react';
import './App.css';  // Import or create a Home.css for styling
import images from './images';

// Functional component for App
function App() {

  // Function to read composer folders and return an array of composers
  const baroqueComposers = require('./composers/baroque.json');
  const classicalComposers = require('./composers/classical.json');
  const romanticComposers = require('./composers/romantic.json');

  return (
    <div className="home-container">
      {/* Styled title */}
      <h1 className="main-title">Algorithmic Analysis of Classical Piano Composers</h1>

      {/* Baroque Period Section */}
      <section className="period-section">
        <h2>Baroque Period (1600-1750)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Baroque period */}
          {baroqueComposers.map((composer) => (
            <ComposerCard key={composer} name={composer} period="Baroque" />
          ))}
        </div>
      </section>

      {/* Classical Period Section */}
      <section className="period-section">
        <h2>Classical Period (1750-1820)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Classical period */}
          {classicalComposers.map((composer) => (
            <ComposerCard key={composer} name={composer} period="Classical" />
          ))}
        </div>
      </section>

      {/* Romantic Period Section */}
      <section className="period-section">
        <h2>Romantic Period (1815-1910)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Romantic period */}
          {romanticComposers.map((composer) => (
            <ComposerCard key={composer} name={composer} period="Romantic" />
          ))}
        </div>
      </section>
    </div>
  );
}


// Component for individual composer cards
const ComposerCard = ({ name}) => {
  return (
    <div className="composer-card">
      {/* Composer image */}
      <img src={images[name]} alt={''} />

      {/* Composer name */}
      <p>{name}</p>
    </div>
  );
};
// Export the App component
export default App;
