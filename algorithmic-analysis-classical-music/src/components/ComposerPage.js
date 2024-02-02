import React from 'react';
import './ComposerPage.css';  // Create a ComposerPage.css for styling

const ComposerPage = () => {
  // Replace the placeholder values with actual data
  const composerData = {
    name: 'J.S. Bach',
    image: 'images/j-s-bach.jpg',
    basicInfo: 'Johann Sebastian Bach (1685-1750) was a German composer and musician...',
    musicDetails: 'Bach composed a vast amount of music, including works for organ, keyboard, and orchestral...',
    chromaticismScores: 'Chromaticism Scores: 8.5/10',
    avgBpm: 'Average BPM: 120',
    keyChanges: 'Key Changes: C major, D minor, G major, A minor, ...',
    leaderboard: 'Favorite Keys Leaderboard: C major, G major, D minor, ...',
  };

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

      {/* Visualizations using matplotlib or other libraries */}
      {/* Include components or code for matrices and histograms here */}
    </div>
  );
};

export default ComposerPage;
