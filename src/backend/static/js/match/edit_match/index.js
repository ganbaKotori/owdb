console.log('heroes json', ow_heroes_json);

const current_user_friends = [];
console.log('match_json 1', ow_match_json);
const match_users_data = ow_match_json.users;
const match_rounds_data = ow_match_json.rounds;
const match_ow_map = ow_match_json.map_played;

console.log('ow_maps', ow_maps_json);
console.log('ow_map_mode', ow_map_modes_json);

const ow_maps = [];
const ow_map_modes = [];

ow_map_modes_json.forEach((ow_map_mode) => {
	let { id, name, max_score } = ow_map_mode;
	let new_map_mode = new OverwatchMapMode(id, name, max_score);

	ow_map_modes.push(new_map_mode);
});

ow_maps_json.forEach((ow_map_data) => {
	let mode_data = ow_map_data.map_mode;
	let ow_map_mode = new OverwatchMapMode(mode_data.id, mode_data.name, mode_data.max_score);
	let ow_map = new OverwatchMap(ow_map_data.id, ow_map_data.name, ow_map_mode, ow_map_data.image_location);

	ow_maps.push(ow_map);
});

const ow_heroes = [];

ow_heroes_json.forEach((h) => {
	let h_role = h.hero_role;
	let hero_role = new HeroRole(h_role.id, h_role.title);
	let hero = new Hero(h.id, h.name, hero_role);

	ow_heroes.push(hero);
});

console.log('hero objs', ow_heroes);

let match_users = [];
let match_rounds = [];

match_users_data.forEach((match_user_data) => {
	let { id } = match_user_data;
	let username = match_user_data.user.username;
	let user_id = match_user_data.user.id;
	let hero_manager = new UserHeroManager();
	let user = new User(id, username, hero_manager, user_id);
	match_users.push(user);
});
match_rounds_data.forEach((match_round_data, index) => {
	let { phase, score } = match_round_data;
	// let match_round = new MatchRound(phase, score, index);
	// match_rounds.push(match_round);
});

let map_id = match_ow_map.id;
let map_name = match_ow_map.name;

let map_mode_id = match_ow_map.map_mode.id;
let map_mode_name = match_ow_map.map_mode.name;
let map_mode_max_score = match_ow_map.map_mode.max_score;

let ow_map_mode = new OverwatchMapMode(map_mode_id, map_mode_name, map_mode_max_score);

let ow_map = new OverwatchMap(map_id, map_name, ow_map_mode, 'FILE LOCATION');

console.log(ow_maps);
let map_manager = new MapManager(ow_maps);

let match_user_manager = new MatchUserManager(match_users, current_user_id);
let match_round_manager = new MatchRoundManager(match_rounds);
let match_map_manager = new MatchMapManager(ow_map);
let match = new Match(match_user_manager, match_round_manager, match_map_manager);
console.log('match_class', match);
console.log('current match user', match.get_current_match_user());
console.log('tagged friends', match.get_tagged_friends());
console.log('map manager', map_manager);

const MATCH_ROUND_LIST_CLASSNAME = '.match-round-list';

match_rounds2 = match.get_rounds();
console.log('match rounds', match_rounds2);
// match_rounds2.forEach((m, index) => {
// 	render_match_round(MATCH_ROUND_LIST_CLASSNAME, m.get_phase(), m.get_score(), index);
// });

const match_manager = new MatchManager(match);
const render_manager = new RenderManager(match);
jq(match_manager, render_manager);
