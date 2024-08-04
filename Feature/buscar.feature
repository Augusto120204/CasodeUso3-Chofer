Feature: Buscar chofer

  Scenario: Buscar un chofer existente
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Escribir el nombre a buscar Alexander
    Then Visualizar el chofer buscado

  Scenario: Buscar un chofer inexistente
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Escribir el nombre a buscar Alma
    Then Visualizar el chofer buscado