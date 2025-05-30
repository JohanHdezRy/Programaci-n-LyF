
% definir condiciones
humedad(baja).
temperatura(35).
hora(20).
probabilidad_lluvia(false).

%regla: es una hora adecuada?
hora_adecuada :- hora(H), (H<10 ; H>18).

%regla principal: cuando se debe de activar el riego
activar_riego :-
    humedad(baja),
    probabilidad_lluvia(false),
    hora_adecuada.

%diagnostico del sistema
estado_riego('Activado'):- activar_riego.
estado_riego('No activado'):- \+ activar_riego.


%regla para alerta de temperatura
alerta_calor :-
    temperatura(T),
    T >=32.

%mensaje de alerta
recomendacion :-
    alerta_calor, !,
    writeln('Alerta: Riego activado con alta temperatura.'),
    
recomendacion :-
    writeln('Sin recomendaciones especiales.').    