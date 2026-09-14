# Thesis-Failure / Opposite-Breakout Signal

## Purpose
This research concept captures cases where a technically reasonable setup fails to produce the move it should have produced. The failure itself becomes information.

The core observation is simple:

> If price has multiple reasons to move in one direction and repeatedly refuses to do so, the probability of an opposite-direction breakout may be rising.

This is particularly important for 0DTE SPY/QQQ credit spreads because gamma makes delayed invalidation expensive.

## Candidate bearish-to-bullish sequence
1. Higher-timeframe regime is bearish or a bearish reversal setup forms.
2. Price rejects resistance or forms an apparent reversal pattern.
3. RSI/SQZMOM or similar momentum indicators weaken.
4. Expected downside does not materialize over roughly 3-5 completed 5-minute candles.
5. Price forms higher lows or repeatedly tests resistance without breaking down.
6. The reversal neckline or structural invalidation never confirms.
7. 15-minute bias may flip bullish while 1H/4H/Daily remain bearish.
8. VIX may fall and/or DXY/cross-asset conditions become more supportive.
9. Price breaks the repeatedly tested resistance with BOS/CHoCH.
10. Volume and/or momentum re-expands in the breakout direction.

The bullish-to-bearish case uses the exact mirror logic.

## Candidate research features
These should be treated as experimental features until enough clean observations exist:
- expected_move_direction
- candles_since_trigger
- follow_through_return
- follow_through_mfe
- follow_through_mae
- failed_breakdown_or_breakout_count
- higher_low_or_lower_high_count
- resistance_or_support_retest_count
- neckline_confirmed
- bias_15m_flip_against_thesis
- sqzmom_deceleration_without_price_followthrough
- sqzmom_reexpansion_opposite_direction
- rsi_rollover_without_price_followthrough
- vix_change_since_trigger
- dxy_change_since_trigger
- opposite_bos_or_choch
- opposite_breakout_volume_expansion

## Candidate labels
For historical testing, measure:
- opposite_breakout_within_15m
- opposite_breakout_within_30m
- opposite_breakout_within_60m
- opposite_move_0_5_atr
- opposite_move_1_0_atr
- original_thesis_recovered_after_stall
- original_short_strike_touched_after_stall
- opposite_credit_spread_would_have_remained_safe

## Adviser behavior
Until validated, this signal is a veto/downweighting mechanism, not an automatic opposite-direction trade trigger.

A live setup should be downgraded when:
- expected follow-through fails for approximately 3-5 completed 5-minute candles;
- momentum weakens but price remains resilient against the thesis;
- structure begins forming higher lows into resistance for bearish setups, or lower highs into support for bullish setups;
- a reversal pattern fails to confirm;
- 15m bias flips against the setup;
- repeated level tests are absorbed;
- opposite-direction BOS/CHoCH occurs with renewed volume or momentum.

When those conditions cluster, the original setup is INVALIDATED rather than repeatedly recycled. Option deltas, credits, strike distance and POP must be refreshed before any new trade is considered.

## Sep 14, 2026 QQQ case-study hypothesis
Observed sequence to preserve for later backtesting:
- large opening decline;
- strong rebound from the opening low;
- apparent resistance/double-top area near the rebound high;
- RSI and SQZMOM decelerated materially;
- expected bearish breakdown did not follow;
- price held structure and formed higher lows;
- 15m bias flipped bullish while higher timeframes remained bearish;
- VIX softened and DXY/cross-asset conditions became more supportive;
- resistance was retested repeatedly;
- QQQ then printed bullish BOS with stronger volume and renewed SQZMOM expansion.

This observation is a case study only. It must not be treated as statistical proof until evaluated chronologically across SPY/QQQ history and held-out data.
