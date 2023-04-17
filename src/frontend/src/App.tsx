import React from 'react';
import { Player } from './components/types/Player';
import TeamComponent from './components/TeamComponent';

const players: Player[] = [
	{ name: 'Player 1', position: 'PG', role: '3', heroes: [] },
	{ name: 'Player 2', position: 'SG', role: '4', heroes: [] },
	{ name: 'Player 3', position: 'SF', role: '2', heroes: [] },
	{ name: 'Player 4', position: 'PF', role: '5', heroes: [] },
	{ name: 'Player 5', position: 'C', role: '1', heroes: [] }
];

const App: React.FC = () => {
	const playerTeam = players.slice(0, 5);
	const enemyTeam = players.slice(5);

	return (
		<div>
			<h2>Player Team</h2>
			<TeamComponent team={playerTeam} />
			<h2>Enemy Team</h2>
			<TeamComponent team={enemyTeam} />
		</div>
	);
};

export default App;
