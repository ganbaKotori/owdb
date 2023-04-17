import React from 'react';
import { Player } from './types/Player';
import PlayerComponent from './PlayerComponent';

interface Props {
	team: Player[];
}

const TeamComponent: React.FC<Props> = ({ team }) => {
	return <div>{team.map((player, index) => <PlayerComponent key={index} player={player} />)}</div>;
};

export default TeamComponent;
