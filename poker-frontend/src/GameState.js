import React from 'react';

function GameState({ gameState }) {
    return (
        <div>
            <h2>Game State</h2>
            <p>Player Tokens: {gameState.player_tokens}</p>
            <p>Opponent Tokens: {gameState.opponent_tokens}</p>
            <p>Pot: {gameState.pot}</p>
            <p>Community Cards: {gameState.community_cards.join(', ')}</p>
            <p>Your Hand: {gameState.player_hand.join(', ')}</p>
        </div>
    );
}

export default GameState;
