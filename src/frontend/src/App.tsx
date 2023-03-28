import React, { useState } from 'react';
import './App.css';
import SelectHero from './SelectHero';

const App: React.FC = () => {
	const [ selectedHero, setSelectedHero ] = useState<string>('Solder 76');

	const handleHeroChange = (hero: string) => {
		setSelectedHero(hero);
	};

	return (
		<div>
			<SelectHero
				options={[ 'Soldier 76', 'Ana', 'D.va' ]}
				label="Select a Hero"
				value={selectedHero}
				onChange={handleHeroChange}
			/>
			<p>You selected {selectedHero}</p>
		</div>
	);
};

export default App;
