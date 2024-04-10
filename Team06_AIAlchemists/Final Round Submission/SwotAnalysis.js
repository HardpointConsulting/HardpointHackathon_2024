import React from 'react';
import './SwotAnalysis.css';

const SwotAnalysis = () => {
  return (
    <div className="swot-container">
      <div className="swot-boxes">
        <div className="box">
          <h3>Strength</h3>
          <textarea placeholder="" readOnly></textarea>
        </div>
        <div className="box">
          <h3>Weakness</h3>
          <textarea placeholder="" readOnly></textarea>
        </div>
        <div className="box">
          <h3>Opportunities</h3>
          <textarea placeholder="" readOnly></textarea>
        </div>
        <div className="box">
          <h3>Threats</h3>
          <textarea placeholder="" readOnly></textarea>
        </div>
      </div>
      <div className="general-inference">
        <h2>General Inference</h2>
        <textarea placeholder="" readOnly></textarea>
      </div>
    </div>
  );
};

export default SwotAnalysis;