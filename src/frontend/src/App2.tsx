import React, { useState } from 'react';
import './App.css';
import SelectHero from './components/SelectHeroRole';

const App: React.FC = () => {
	const [ selectedHero, setSelectedHero ] = useState<string>('Solder 76');

	const handleHeroChange = (hero: string) => {
		setSelectedHero(hero);
	};

	const propsArray = [
		{ options: [ 'Damage', 'Tank', 'Support' ] },
		{ options: [ 'Damage', 'Tank', 'Support' ] },
		{ options: [ 'Damage', 'Tank', 'Support' ] }
	];

	const roles = [ 'Damage', 'Tank', 'Support' ];

	return (
		<div>
			{propsArray.map((props, index) => (
				<SelectHero
					key={index}
					options={roles}
					label="Select a Hero Role"
					value={selectedHero}
					onChange={handleHeroChange}
				/>
			))}
			<p>You selected {selectedHero}</p>
		</div>
	);
};

export default App;
