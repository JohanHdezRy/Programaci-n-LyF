% Definición de zonas de riego con sus características
zona(1, jardin_m, 30, 50).
zona(2, jardin_p, 40, 60).
zona(3, flores, 25, 45).
zona(4, huerto, 45, 65).

% Inicialización de valores de ejemplo
hora(20).
probabilidad_lluvia(false).
velocidad_viento(5).

%valores por zona
humedad_zona(1, 25).
humedad_zona(2, 38).
humedad_zona(3, 20).
humedad_zona(4, 50).

temperatura_zona(1, 35).
temperatura_zona(2, 32).
temperatura_zona(3, 30).
temperatura_zona(4, 28).

% Regla: ¿Es una hora adecuada para regar?
hora_adecuada :-
    hora(H),
    (H >= 5, H =< 9 ; H >= 18, H =< 22).

% Regla: ¿Condiciones climáticas adecuadas?
condiciones_climaticas_adecuadas :-
    probabilidad_lluvia(false),
    velocidad_viento(V), V < 15. % No regar si hay mucho viento

% Regla: ¿La zona necesita riego?
necesita_riego(Zona) :-
    zona(Zona, _, Min, Max),
    humedad_zona(Zona, H),
    H < Min. % Humedad por debajo del mínimo ideal

% Regla principal: activar riego para una zona específica
activar_riego(Zona) :-
    necesita_riego(Zona),
    condiciones_climaticas_adecuadas,
    hora_adecuada.

% Diagnóstico del sistema por zona
estado_riego(Zona, 'Activado') :- activar_riego(Zona).
estado_riego(Zona, 'No activado') :- \+ activar_riego(Zona).

% Alertas de temperatura por zona
alerta_temperatura(Zona) :-
    temperatura_zona(Zona, T),
    T >= 35, !,
    writeln('ALERTA: Temperatura extremadamente alta en zona '),
    write(Zona), nl.

alerta_temperatura(Zona) :-
    temperatura_zona(Zona, T),
    T >= 32, !,
    writeln('Advertencia: Temperatura alta en zona '),
    write(Zona), nl.

%alerta_temperatura(_). % No hay alerta para otras temperaturas

% Recomendaciones
recomendacion(Zona) :-
    activar_riego(Zona),
    temperatura_zona(Zona, T), T >= 32, !,
    zona(Zona, Tipo, _, _),
    write('Recomendación: Regar zona '), write(Zona),
    write(' ('), write(Tipo), write(') en horas de la tarde/noche. '),
    writeln('Evitar riego al mediodía por alta temperatura.').

recomendacion(Zona) :-
    activar_riego(Zona), !,
    zona(Zona, Tipo, _, _),
    write('Recomendación: Regar zona '), write(Zona),
    write(' ('), write(Tipo), write(') según programa establecido.'), nl.

recomendacion(Zona) :-
    humedad_zona(Zona, H),
    zona(Zona, _, Min, _),
    H > Min, !,
    write('Recomendación: Zona '), write(Zona),
    writeln(' tiene suficiente humedad. No se requiere riego.').

recomendacion(Zona) :-
    \+ condiciones_climaticas_adecuadas, !,
    write('Recomendación: Zona '), write(Zona),
    writeln(' necesita riego pero las condiciones climáticas no son óptimas.').

recomendacion(_) :-
    writeln('Sin recomendaciones especiales.').

