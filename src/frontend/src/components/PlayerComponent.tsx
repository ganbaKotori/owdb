import React, { useState } from 'react';
import { Player } from './types/Player';
import SelectHero from './SelectHeroRole';

interface Props {
	player: Player;
}

const PlayerComponent: React.FC<Props> = ({ player }) => {
	const [ selectedHero, setSelectedHero ] = useState<string>('Solder 76');

	const options = [ 'Damage', 'Tank', 'Support' ];

	const handleHeroChange = (hero: string) => {
		setSelectedHero(hero);
	};
	return (
		<div>
			<label>
				Name:
				<input type="text" value={player.name} />
			</label>
			<br />
			<label>
				Position:
				<select value={player.position}>
					<option value="PG">Point Guard</option>
					<option value="SG">Shooting Guard</option>
					<option value="SF">Small Forward</option>
					<option value="PF">Power Forward</option>
					<option value="C">Center</option>
				</select>
			</label>
			<br />
			<SelectHero options={options} label="Select a Hero Role" value={selectedHero} onChange={handleHeroChange} />
		</div>
	);
};

export default PlayerComponent;
