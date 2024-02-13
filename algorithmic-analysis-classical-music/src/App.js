// Import necessary dependencies
import React, { useState } from 'react';
import './App.css';  // Import or create a Home.css for styling

import schumannJson from './composers/json/schumann.json';
import borodinJson from './composers/json/borodin.json';
import clementiJson from './composers/json/clementi.json';
import haydnJson from './composers/json/haydn.json';
import mussorgskyJson from './composers/json/mussorgsky.json';
import tchaikovskyJson from './composers/json/tchaikovsky.json';
import albenizJson from './composers/json/albeniz.json';
import brahmsJson from './composers/json/brahms.json';
import debussyJson from './composers/json/debussy.json';
import lisztJson from './composers/json/liszt.json';
import rachmaninovJson from './composers/json/rachmaninov.json';
import bachJson from './composers/json/bach.json';
import burgmuellerJson from './composers/json/burgmueller.json';
import granadosJson from './composers/json/granados.json';
import mendelssohnJson from './composers/json/mendelssohn.json';
import ravelJson from './composers/json/ravel.json';
import beethovenJson from './composers/json/beethoven.json';
import chopinJson from './composers/json/chopin.json';
import griegJson from './composers/json/grieg.json';
import mozartJson from './composers/json/mozart.json';
import schubertJson from './composers/json/schubert.json';

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

const composerDataMap = {
  Schumann: schumannJson,
  Borodin: borodinJson,
  Clementi: clementiJson,
  Haydn: haydnJson,
  Mussorgsky: mussorgskyJson,
  Tchaikovsky: tchaikovskyJson,
  Albeniz: albenizJson,
  Brahms: brahmsJson,
  Debussy: debussyJson,
  Liszt: lisztJson,
  Rachmaninov: rachmaninovJson,
  Bach: bachJson,
  Burgmueller: burgmuellerJson,
  Granados: granadosJson,
  Mendelssohn: mendelssohnJson,
  Ravel: ravelJson,
  Beethoven: beethovenJson,
  Chopin: chopinJson,
  Grieg: griegJson,
  Mozart: mozartJson,
  Schubert: schubertJson,
};

// Functional component for App
function App() {
  const [composerData, setComposerData] = useState(null);
  const [isModalVisible, setIsModalVisible] = useState(false);

  const handleComposerClick = (composerName) => {
    const data = composerDataMap[composerName];
    setComposerData(data);
    setIsModalVisible(true); // Show the modal
  };

  const handleCloseModal = () => {
    setIsModalVisible(false); // Hide the modal
  };

  return (
    <div className="home-container">
      {/* Styled title */}
      <h1 className="main-title">Algorithmic Analysis of Classical Piano Composers</h1>

      {/* Baroque Period Section */}
      <section className="period-section">
        <h2>Baroque Period (1600-1750)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Baroque period */}
          <ComposerCard key={'Bach'} name={'Bach'} image={bach} onClick={() => handleComposerClick('Bach')}/>
        </div>
      </section>

      {/* Classical Period Section */}
      <section className="period-section">
        <h2>Classical Period (1750-1820)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Classical period */}
          <ComposerCard key={'Beethoven'} name={'Beethoven'} image={beethoven} onClick={() => handleComposerClick('Beethoven')}/>
          <ComposerCard key={'Clementi'} name={'Clementi'} image={clementi} onClick={() => handleComposerClick('Clementi')}/>
          <ComposerCard key={'Haydn'} name={'Haydn'} image={haydn} onClick={() => handleComposerClick('Haydn')}/>
          <ComposerCard key={'Mozart'} name={'Mozart'} image={mozart} onClick={() => handleComposerClick('Mozart')}/>
        </div>
      </section>

      {/* Romantic Period Section */}
      <section className="period-section">
        <h2>Romantic Period (1815-1910)</h2>
        <div className="composer-grid">
          {/* Composer cards for the Romantic period */}
          <ComposerCard key={'Albeniz'} name={'Albeniz'} image={albeniz} onClick={() => handleComposerClick('Albeniz')}/>
          <ComposerCard key={'Borodin'} name={'Borodin'} image={borodin} onClick={() => handleComposerClick('Borodin')}/>
          <ComposerCard key={'Brahms'} name={'Brahms'} image={brahms} onClick={() => handleComposerClick('Brahms')}/>
          <ComposerCard key={'Burgmueller'} name={'Burgmueller'} image={burgmueller} onClick={() => handleComposerClick('Burgmueller')}/>
          <ComposerCard key={'Chopin'} name={'Chopin'} image={chopin} onClick={() => handleComposerClick('Chopin')}/>
          <ComposerCard key={'Debussy'} name={'Debussy'} image={debussy} onClick={() => handleComposerClick('Debussy')}/>
          <ComposerCard key={'Granados'} name={'Granados'} image={granados} onClick={() => handleComposerClick('Granados')}/>
          <ComposerCard key={'Grieg'} name={'Grieg'} image={grieg} onClick={() => handleComposerClick('Grieg')}/>
          <ComposerCard key={'Liszt'} name={'Liszt'} image={liszt} onClick={() => handleComposerClick('Liszt')}/>
          <ComposerCard key={'Mendelssohn'} name={'Mendelssohn'} image={mendelssohn} onClick={() => handleComposerClick('Mendelssohn')}/>
          <ComposerCard key={'Mussorgsky'} name={'Mussorgsky'} image={mussorgsky} onClick={() => handleComposerClick('Mussorgsky')}/>
          <ComposerCard key={'Rachmaninov'} name={'Rachmaninov'} image={rachmaninov} onClick={() => handleComposerClick('Rachmaninov')}/>
          <ComposerCard key={'Ravel'} name={'Ravel'} image={ravel} onClick={() => handleComposerClick('Ravel')}/>
          <ComposerCard key={'Schubert'} name={'Schubert'} image={schubert} onClick={() => handleComposerClick('Schubert')}/>
          <ComposerCard key={'Schumann'} name={'Schumann'} image={schumann} onClick={() => handleComposerClick('Schumann')}/>
          <ComposerCard key={'Tchaikovsky'} name={'Tchaikovsky'} image={tchaikovsky} onClick={() => handleComposerClick('Tchaikovsky')}/>
        </div>
      </section>

      {isModalVisible && (
        <ComposerModal data={composerData} onClose={handleCloseModal} />
      )}

    </div>
  );
}


const ComposerCard = ({name, image, onClick}) => {
  return (
    // Added onClick event handler to make the card clickable
    <div className="composer-card" onClick={onClick}>
      <img src={image} alt={name} />
      <p>{name}</p>
    </div>
  );
};

function ComposerModal({ data, onClose }) {
  if (!data) return null; // Don't render the modal if there's no data

  return (
    <div className="modal-backdrop">
      <div className="modal-content">
        <button className="close-button" onClick={onClose}>X</button>
        <h2 className="composer-name">{data.name}</h2>
        <div className="composer-details">
          <div className="personal-info">
            <p><strong>Birth:</strong> {data.birth}</p>
            <p><strong>Death:</strong> {data.death}</p>
            <p><strong>Nationality:</strong> {data.nationality}</p>
            <p><strong>Era:</strong> {data.era}</p>
          </div>
          <div className="notable-works">
            <h3 className="section-heading">Notable Works:</h3>
            <ul>
              {data.notableWorks.map((work, index) => (
                <li key={index}>{work}</li>
              ))}
            </ul>
          </div>
        </div>
        <div className="biography">
          <h3 className="section-heading">Biography:</h3>
          <p>{data.biography}</p>
        </div>
        <h3 className="section-heading">Pieces:</h3>
        <div className="pieces">
          {Object.entries(data.pieces).map(([filename, pieceInfo]) => (
            <div key={filename} className="piece">
              <h4 className="piece-title">{pieceInfo.title}</h4>
              <div className="piece-images">
                {pieceInfo.pitch_histogram && (
                  <img src={`data:image/png;base64,${pieceInfo.pitch_histogram}`} alt="Pitch Histogram" className="piece-image" />
                )}
                {pieceInfo.transition_matrix && (
                  <img src={`data:image/png;base64,${pieceInfo.transition_matrix}`} alt="Transition Matrix" className="piece-image" />
                )}
                {pieceInfo.chroma_matrix && (
                  <img src={`data:image/png;base64,${pieceInfo.chroma_matrix}`} alt="Chroma Matrix" className="piece-image" />
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// Export the App component
export default App;
