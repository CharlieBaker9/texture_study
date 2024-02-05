// Import necessary dependencies
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';  // Import or create a Home.css for styling

// import ComposerPage from './components/ComposerPage';

import schumann from './images/Schumann.jpeg';
import borodin from './images/borodin.jpeg';
import clementi from './images/clementi.jpg';
import haydn from './images/haydn.jpg';
import mussorgsky from './images/mussorgsky.jpeg';
import tchaikovsky from './images/tchaikovsky.jpeg';
import albeniz from './images/albeniz.jpeg';
import brahms from './images/brahms.jpeg';
import debussy from './images/debussy.jpeg';
import liszt from './images/liszt.jpeg';
import rachmaninov from './images/rachmaninov.jpeg';
import bach from './images/bach.jpg';
import burgmueller from './images/burgmueller.jpeg';
import granados from './images/granados.jpeg';
import mendelssohn from './images/mendelssohn.jpeg';
import ravel from './images/ravel.jpeg';
import beethoven from './images/beethoven.jpg';
import chopin from './images/chopin.jpeg';
import grieg from './images/grieg.jpeg';
import mozart from './images/mozart.jpg';
import schubert from './images/schubert.jpeg';

// Functional component for App
function App() {
  return (
    <Router>
      <div className="home-container">
        {/* Styled title */}
        <h1 className="main-title">Algorithmic Analysis of Classical Piano Composers</h1>

        <Routes>
          {/* Baroque Period Section */}
          <Route path="/">
            <section className="period-section">
              <h2>Baroque Period (1600-1750)</h2>
              <div className="composer-grid">
                {/* Composer cards for the Baroque period */}
                <ComposerCard key={'Bach'} name={'Bach'} image={bach} />
              </div>
            </section>

            {/* Classical Period Section */}
            <section className="period-section">
              <h2>Classical Period (1750-1820)</h2>
              <div className="composer-grid">
                {/* Composer cards for the Classical period */}
                <ComposerCard key={'Beethoven'} name={'Beethoven'} image={beethoven} />
                <ComposerCard key={'Clementi'} name={'Clementi'} image={clementi} />
                <ComposerCard key={'Haydn'} name={'Haydn'} image={haydn} />
                <ComposerCard key={'Mozart'} name={'Mozart'} image={mozart} />
              </div>
            </section>

            {/* Romantic Period Section */}
            <section className="period-section">
              <h2>Romantic Period (1815-1910)</h2>
              <div className="composer-grid">
                {/* Composer cards for the Romantic period */}
                <ComposerCard key={'Albeniz'} name={'Albeniz'} image={albeniz} />
                <ComposerCard key={'Borodin'} name={'Borodin'} image={borodin} />
                <ComposerCard key={'Brahms'} name={'Brahms'} image={brahms} />
                <ComposerCard key={'Burgmueller'} name={'Burgmueller'} image={burgmueller} />
                <ComposerCard key={'Chopin'} name={'Chopin'} image={chopin} />
                <ComposerCard key={'Debussy'} name={'Debussy'} image={debussy} />
                <ComposerCard key={'Granados'} name={'Granados'} image={granados} />
                <ComposerCard key={'Grieg'} name={'Grieg'} image={grieg} />
                <ComposerCard key={'Liszt'} name={'Liszt'} image={liszt} />
                <ComposerCard key={'Mendelssohn'} name={'Mendelssohn'} image={mendelssohn} />
                <ComposerCard key={'Mussorgsky'} name={'Mussorgsky'} image={mussorgsky} />
                <ComposerCard key={'Rachmaninov'} name={'Rachmaninov'} image={rachmaninov} />
                <ComposerCard key={'Ravel'} name={'Ravel'} image={ravel} />
                <ComposerCard key={'Schubert'} name={'Schubert'} image={schubert} />
                <ComposerCard key={'Schumann'} name={'Schumann'} image={schumann} />
                <ComposerCard key={'Tchaikovsky'} name={'Tchaikovsky'} image={tchaikovsky} />
              </div>
            </section>
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

// Component for individual composer cards
const ComposerCard = ({name, image}) => {
  // const navigate = useNavigate();

  // const handleCardClick = () => {
  //   // Navigate to the ComposerPage with the composer's name as a parameter
  //   navigate(`/composer/${name.toLowerCase()}`);
  // };
  return (
    <div className="composer-card">
      <img src={image} alt={''} />
      <p>{name}</p>
    </div>
  );
};
// Export the App component
export default App;
