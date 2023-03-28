class MatchRoundPhase {
    static Attack = new MatchRoundPhase("Attack");
    static Defend = new MatchRoundPhase("Defend");
  
    constructor(name) {
      this.name = name
    }
  }
  