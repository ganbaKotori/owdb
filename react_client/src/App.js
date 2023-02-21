// src/App.js
import React from 'react';
import Table, { SelectColumnFilter } from './Table';

const getMatches = () => {
	return fetch('/api/match', {
		headers: {
			Cookie:
				'session=.eJwljkFqQzEMRO_idRe2ZFlyLvORLImEQgv_J6vSu8elm4EZHsz7KUeecd3L7Xm-4qMcDy-3EtgrRZckJSar4KA1Wxh0qa0FQQJO9OCRfXNThYGnujcfyIRm3URJEI3Xor40AKaOKlidjRmmm6VNTvA-ppCA48Bk5UVQtsjrivPfZuy6rjOP5_dnfO0BBg2Ozk3kLwZ4SkPPVKmy2jKelvu3_L4Bh-Y-vA.Y_Gmwg.E5Zx6LxbXjKCs-5vJ8rXTZV-VRs'
		}
	})
		.then((response) => response.json())
		.then((data) => {
			return data;
		});
};

const formatMatchData = (match) => {
	return {
		map: match.map_name ? match.map_name : 'No Map',
		role: match.hero_role ? match.hero_role : 'No Role',
		heroes: '',
		final: '',
		date_played: ''
	};
};

const getData = () => {
	const data = [
		{
			name: 'Jane Cooper',
			email: 'jane.cooper@example.com',
			title: 'Regional Paradigm Technician',
			department: 'Optimization',
			status: 'Active',
			role: 'Admin',
			age: 23,
			imgUrl:
				'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		},
		{
			name: 'Cody Fisher',
			email: 'cody.fisher@example.com',
			title: 'Product Directives Officer',
			department: 'Intranet',
			status: 'Active',
			role: 'Owner',
			age: 20,
			imgUrl:
				'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		},
		{
			name: 'Esther Howard',
			email: 'esther.howard@example.com',
			title: 'Forward Response Developer',
			department: 'Directives',
			status: 'Active',
			role: 'Member',
			age: 29,
			imgUrl:
				'https://images.unsplash.com/photo-1520813792240-56fc4a3765a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		},
		{
			name: 'Jenny Wilson',
			email: 'jenny.wilson@example.com',
			title: 'Central Security Manager',
			department: 'Program',
			status: 'Active',
			role: 'Member',
			age: 28,
			imgUrl:
				'https://images.unsplash.com/photo-1498551172505-8ee7ad69f235?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		},
		{
			name: 'Kristin Watson',
			email: 'kristin.watson@example.com',
			title: 'Lean Implementation Liaison',
			department: 'Mobility',
			status: 'Active',
			role: 'Admin',
			age: 18,
			imgUrl:
				'https://images.unsplash.com/photo-1532417344469-368f9ae6d187?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		},
		{
			name: 'Cameron Williamson',
			email: 'cameron.williamson@example.com',
			title: 'Internal Applications Engineer',
			department: 'Security',
			status: 'Active',
			role: 'Member',
			age: 33,
			imgUrl:
				'https://images.unsplash.com/photo-1566492031773-4f4e44671857?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60'
		}
	];
	return [ ...data, ...data, ...data ];
};

function App() {
	const columns = React.useMemo(
		() => [
			{
				Header: 'Map',
				accessor: 'name'
			},
			{
				Header: 'Role',
				accessor: 'title'
			},
			{
				Header: 'Heroes',
				accessor: 'status'
			},
			{
				Header: 'Final',
				accessor: 'role',
				Filter: SelectColumnFilter, // new
				filter: 'includes' // new
			},
			{
				Header: 'Date',
				accessor: 'age'
			}
		],
		[]
	);

	const data = React.useMemo(() => getData(), []);

	const matches = [];

	let userToken = getMatches();
	userToken.then(function(result) {
		console.log(result); // "Some User token"
		for (var i = 0; i < result.length; i++) {
			console.log(result[i]);
			matches.push(formatMatchData(result[i]));
		}
	});
	console.log('mr', matches);

	return (
		<div className="min-h-screen bg-gray-100 text-gray-900">
			<main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-4">
				<div className="">
					<h1 className="text-xl font-semibold">All Matches</h1>
				</div>
				<div className="mt-4">
					<Table columns={columns} data={data} />
				</div>
			</main>
		</div>
	);
}

export default App;
