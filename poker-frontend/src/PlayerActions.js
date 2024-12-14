import React from 'react';

function PlayerActions({ onAction }) {
    return (
        <div>
            <h2>Actions</h2>
            <button onClick={() => onAction('Call')}>Call</button>
            <button onClick={() => onAction('Raise:50')}>Raise 50</button>
            <button onClick={() => onAction('Fold')}>Fold</button>
        </div>
    );
}

export default PlayerActions;
