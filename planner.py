from model import TravelPlan, ModelConfig
import solver

def pianifica(travel_plan: TravelPlan, config: ModelConfig):
    """
    - prepara l'input per il solver
    - chiama la DP
    - ricostruisce l'output finale
    """

    n = len(travel_plan)

    costs = config.get_cost()
    durations = config.get_durations()

    dp, choise = solver.solve(
        n = n,
        travel_days = travel_plan.days,
        costs = costs,
        durations = durations
    )

    abbonamenti = solver.reconstruct(
        choise = choise,
        durations = durations,
        n = n
    )

    return {
        "costo minimo": dp[0],
        "abbonamenti": abbonamenti
    }