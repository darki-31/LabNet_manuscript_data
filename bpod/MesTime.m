function MesTime
global BpodSystem

% Bpod state machine is very simple and has only two states.
% We need to cennect two BNC port to the measurement RasPi. One for the external trigger event "In1" and for the response "OUT1".
% On the RasPi we need to start the "perf_test" program from "examples/cpp/perf_test" folder.
%
% state machine flow description:
% enter the state 'WaitForOnState'
% wait until the external triger on BNC1 is high
% enter the state "TurnOnState" -> turn output BNCs on
% wait until BNC1 is low or the timer is up
% on leave output BNCs go automatically off
% enter the state 'WaitForOnState' -> repeat

sma = NewStateMatrix();
sma = AddState(sma, 'Name', 'WaitForOnState', ...
    'Timer', 0,...
    'StateChangeConditions', {'BNC1High', 'TurnOnState'},...
    'OutputActions', {});
sma = AddState(sma, 'Name', 'TurnOnState', ...
    'Timer', 0.1,...
    'StateChangeConditions', {'Tup', 'WaitForOnState', 'BNC1Low', 'WaitForOnState'},...
    'OutputActions', {'BNCState', 3});

SendStateMatrix(sma);
RunStateMatrix;
