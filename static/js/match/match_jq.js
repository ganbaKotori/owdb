$(document).ready(function () {
  $('.ow-hero-check').hide();
  
  $(".ow-hero-role-radio-btn").on("change", function () {
    console.log($(this).val());
    $(".ow-hero-check").hide();
    $(`.ow-hero-check-role-${$(this).val()}`).show();
  });

  $(".add-round-btn").on("click", function () {
    match.add_round("ATTACK", 0);
  });

  $(document).on("click", ".minus-btn", function () {
    let round_id = $(this).data("round-id");
    let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
    if (score - 1 >= 0) {
      $(`#match_rounds-${round_id}-score-obtained`).val(score - 1);
    }
    console.log(score);
    // get_total_team_score();
    update_match_final_results();
  });

  $(document).on("click", ".plus-btn", function () {
    let round_id = $(this).data("round-id");
    let score = parseInt($(`#match_rounds-${round_id}-score-obtained`).val());
    if (score + 1 <= match.current_map_selected.max_score) {
      $(`#match_rounds-${round_id}-score-obtained`).val(score + 1);
    }
    console.log(score);
    // get_total_team_score();
    update_match_final_results();
  });

  $(".add_tagged-friend-btn").on("click", function () {
    $(".tagged-friend-select").each(function () {
      console.log($(this).val());
    });
    match.add_tagged_friend();
  });

  $(document).on("click", ".delete-match-round-btn", function () {
    match.remove_round($(this).parent().parent().parent());
  });

  $(document).on("click", ".delete-tagged-friend-btn", function () {
    console.log("clicked");
    match.remove_tagged_friend($(this).parent().parent().parent());
  });

  $(document).on("click", ".attack-btn", function () {
    let round_id = $(this).data("round-id");
    console.log(round_id);
    $(`#match_rounds-${round_id}-score-text`).text("Team Score");
    $(`#match_rounds-${round_id}-score-obtained`).removeClass(
      "match-round-score-defend"
    );
    $(`#match_rounds-${round_id}-score-obtained`).addClass(
      "match-round-score-attack"
    );
    update_match_final_results();
  });

  $(document).on("click", ".defend-btn", function () {
    let round_id = $(this).data("round-id");
    console.log(round_id, "defend");
    $(`#match_rounds-${round_id}-score-text`).text("Enemy Score");
    $(`#match_rounds-${round_id}-score-obtained`).removeClass(
      "match-round-score-attack"
    );
    $(`#match_rounds-${round_id}-score-obtained`).addClass(
      "match-round-score-defend"
    );
    update_match_final_results();
  });

  $("#ow_map_select").on("change", function () {
    console.log($("#ow_map_select option:selected").text());
    $("#map-image").attr(
      "src",
      map_images[$("#ow_map_select option:selected").text()]
    );
    $("#map-title-text").text($("#ow_map_select option:selected").text());
    let current_map_id = parseInt($("#ow_map_select").val());
    console.log(current_map_id);
    let map_selected = ow_maps.find((ow_map) => ow_map.id === current_map_id);
    match.set_current_ow_map(map_selected);
    console.log(match.current_map_selected);
  });

  $(".match-round-score").on("change", function () {
    let current_max_score = match.current_map_selected.max_score;
    console.log(current_max_score);
    let current_score = $(this).val();
    console.log(current_score);
    if (current_score > current_max_score) {
      $(this).val(current_max_score);
    }
    //get_total_team_score();
  });

  $(document).on("click", ".control-enemy-plus", function () {
    match.add_round((phase = "DEFEND"), (score = 1));
    update_match_final_results();
  });

  $(document).on("click", ".control-enemy-minus", function () {
    const defend_round = match.rounds.findIndex((round) => {
      return round.phase === "DEFEND";
    });
    if (defend_round != null) {
      match.remove_round_by_id(match.rounds[defend_round].id);
      update_match_final_results();
    }
  });

  $(document).on("click", ".control-player-plus", function () {
    match.add_round((phase = "ATTACK"), (score = 1));
    update_match_final_results();
  });

  $(document).on("click", ".control-player-minus", function () {
    const attack_round = match.rounds.findIndex((round) => {
      return round.phase === "ATTACK";
    });
    if (attack_round != null) {
      match.remove_round_by_id(match.rounds[attack_round].id);
      update_match_final_results();
    }
  });

  $(document).on("change", ".match-round-score-attack", function () {
    //get_total_team_score();
    //get_total_enemy_score();
    update_match_final_results();
  });

  $(document).on("change", ".match-round-score-defend", function () {
    console.log("match round score deend is changed");
    //get_total_enemy_score();
    update_match_final_results();
  });

  $(".tag-friends-btn").on("click", async function () {
    // const friends = await get_current_user_friends();
    // console.log(friends)
  });

  $(".today-btn").on("click", async function () {
    $("#date-match-played").val(
      (date.getMonth() > 8
        ? date.getMonth() + 1
        : "0" + (date.getMonth() + 1)) +
        "/" +
        (date.getDate() > 9 ? date.getDate() : "0" + date.getDate()) +
        "/" +
        date.getFullYear()
    );
  });
});
