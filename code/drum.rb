live_loop :listen do
  set_sched_ahead_time! 0.01
end

live_loop :listen do
  message = sync "/play_drum"
  drum = message[:args][0]
  cue :one if drum=="1"
  cue :two if drum=="2"
  cue :three if drum=="3"
  cue :four if drum=="4"
  cue :five if drum=="5"
  cue :six if drum=="6"
end

in_thread do
  loop do
    sync :one
    sample :drum_bass_hard
  end
end
in_thread do
  loop do
    sync :two
    sample :drum_bass_soft
  end
end
in_thread do
  loop do
    sync :three
    sample :drum_cymbal_closed
  end
end
in_thread do
  loop do
    sync :four
    sample :drum_snare_hard
  end
end
in_thread do
  loop do
    sync :five
    sample :drum_splash_hard
  end
end
in_thread do
  loop do
    sync :six
    sample :drum_splash_soft
  end
end

