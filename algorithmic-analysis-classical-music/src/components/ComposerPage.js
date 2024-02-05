import React, { useEffect, useState } from 'react';
import './ComposerPage.css';

const ComposerPage = ({ composerName }) => {
  const [composerData, setComposerData] = useState(null);

  useEffect(() => {
    // Fetch data from your JSON file or API using composerName
    // For simplicity, I'll assume you have a JSON file named composers.json
    fetch(`/path/to/composers.json`)
      .then((response) => response.json())
      .then((data) => {
        const selectedComposer = data.find((composer) => composer.name === composerName);

        if (selectedComposer) {
          setComposerData(selectedComposer);
        } else {
          // Handle case when composer is not found
          console.error(`Composer '${composerName}' not found`);
        }
      })
      .catch((error) => console.error('Error fetching composer data:', error));
  }, [composerName]);

  if (!composerData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="composer-page-container">
      <div className="composer-header">
        <img src={composerData.image} alt={composerData.name} />
        <h1>{composerData.name}</h1>
      </div>

      <div className="composer-info">
        <section className="basic-info">
          <h2>Basic Information</h2>
          <p>{composerData.basicInfo}</p>
        </section>

        <section className="music-details">
          <h2>Music Details</h2>
          <p>{composerData.musicDetails}</p>
        </section>
      </div>

      <div className="composer-stats">
        <section className="chromaticism-scores">
          <h2>Chromaticism Scores</h2>
          <p>{composerData.chromaticismScores}</p>
        </section>

        <section className="avg-bpm">
          <h2>Average BPM</h2>
          <p>{composerData.avgBpm}</p>
        </section>

        <section className="key-changes">
          <h2>Key Changes</h2>
          <p>{composerData.keyChanges}</p>
        </section>

        <section className="leaderboard">
          <h2>Favorite Keys Leaderboard</h2>
          <p>{composerData.leaderboard}</p>
        </section>
      </div>
    </div>
  );
};

export default ComposerPage;
