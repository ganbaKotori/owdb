const MAX_TAGGED_FRIENDS = 4;

const match = new Match(current_user_friends);
const ow_maps = [];

ow_maps_data.forEach((ow_map) => {
  let new_map = new OverwatchMap(
    ow_map.id,
    ow_map.name,
    ow_map.map_mode.name,
    ow_map.map_mode.max_score
  );
  ow_maps.push(new_map);
});

const map_images = {
  HOLLYWOOD: "\\static\\assets\\img\\ow_map_img\\hollywood.jpg",
  HAVANA: "\\static\\assets\\img\\ow_map_img\\default.jpg",
  NEPAL: "\\static\\assets\\img\\ow_map_img\\nepal.jpg",
  NUMBANI: "\\static\\assets\\img\\ow_map_img\\numbani.jpg",
  ILIOS: "\\static\\assets\\img\\ow_map_img\\ilios.jpg",
  "BLIZZARD WORLD": "\\static\\assets\\img\\ow_map_img\\blizzard-world.jpg",
  "VOLSKAYA INDUSTRIES":
    "\\static\\assets\\img\\ow_map_img\\volskaya-industries.jpg",
  "KING'S ROW": "\\static\\assets\\img\\ow_map_img\\kings-row.jpg",
  BUSAN: "\\static\\assets\\img\\ow_map_img\\busan.jpg",
  DORADO: "\\static\\assets\\img\\ow_map_img\\dorado.jpg",
  HANAMURA: "\\static\\assets\\img\\ow_map_img\\hanamura.jpg",
  JUNKERTOWN: "\\static\\assets\\img\\ow_map_img\\junkertown.jpg",
  "LIJIANG TOWER": "\\static\\assets\\img\\ow_map_img\\lijiang-tower.jpg",
  OASIS: "\\static\\assets\\img\\ow_map_img\\oasis.jpg",
  RIALTO: "\\static\\assets\\img\\ow_map_img\\rialto.jpg",
  "ROUTE 66": "\\static\\assets\\img\\ow_map_img\\route-66.jpg",
  "TEMPLE OF ANUBIS": "\\static\\assets\\img\\ow_map_img\\temple-of-anubis.jpg",
  "WATCHPOINT: GIBRALTAR":
    "\\static\\assets\\img\\ow_map_img\\watchpoint-gibraltar.jpg",
  EICHENWALDE: "\\static\\assets\\img\\ow_map_img\\eichenwalde.jpg",
};

$(".delete-match-btn").on("click", async function () {
  if (confirm("Are you sure you want to delete this match?") == true) {
    let match_id = $(this).data("match-id");
    let delete_match_response = await delete_match(match_id);
    if (delete_match_response.status == 200) {
      alert("Match Deleted!");
      $(`#match-${match_id}-tr`).slideUp();
    }
    console.log(delete_match_response.status);
  } else {
  }
});

const delete_match = async (match_id) => {
  const response = await fetch(`/api/match/${match_id}`, {
    method: "DELETE",
  });
  return response;
};

const get_friends_options = (friends) => {
  let friends_options_str = "";
  friends.forEach((friend) => {
    friends_options_str += `<option value="${friend}">${friend}</option>`;
  });
  return friends_options_str;
};

let get_total_team_score = () => {
  let total_team_score = 0;
  $(".match-round-score-attack").each(function () {
    if ($(this).val() != null) {
      total_team_score += parseInt($(this).val());
    }
  });
  $("#team-score-total").text(total_team_score);
  $("#team-score-total").addClass("confirm_selection");
  $("#team-score-total").on("animationend", function () {
    $(this).removeClass("confirm_selection");
  });
  return total_team_score;
};

let get_total_enemy_score = () => {
  let total_enemy_score = 0;
  $(".match-round-score-defend").each(function () {
    if ($(this).val() != null) {
      total_enemy_score += parseInt($(this).val());
    }
  });
  $("#enemy-score-total").text(total_enemy_score);
  $("#enemy-score-total").addClass("confirm_selection");
  $("#enemy-score-total").on("animationend", function () {
    $(this).removeClass("confirm_selection");
  });
  return total_enemy_score;
};

let update_match_final_results = () => {
  let total_enemy_score = get_total_enemy_score();
  let total_team_score = get_total_team_score();
  if (total_team_score > total_enemy_score) {
    $("#match-final-result").text("VICTORY");
  } else if (total_team_score < total_enemy_score) {
    $("#match-final-result").text("DEFEAT");
  } else {
    $("#match-final-result").text("DRAW");
  }
};

function padTo2Digits(num) {
  return num.toString().padStart(2, "0");
}

function formatDate(date) {
  return (
    [
      date.getFullYear(),
      padTo2Digits(date.getMonth() + 1),
      padTo2Digits(date.getDate()),
    ].join("-") +
    " " +
    [padTo2Digits(date.getHours()), padTo2Digits(date.getMinutes())].join(":")
  );
}

flatpickr("#datetime", {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
  altInput: true,
  altFormat: "F j, Y @ h:i K",
  defaultDate: formatDate(new Date()),
  minuteIncrement: 1,
});
