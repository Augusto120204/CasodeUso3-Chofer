Feature: Agregar chofer

  Scenario: Agregar un chofer
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón agregar
    And Rellenar el campo Nombre Pepe
    And Rellenar el campo Apellido Rios
    And Rellenar el campo Número de Telefono 0999893860
    And Seleccionar el sexo Masculino
    And Rellenar el campo Cédula 1727925602
    And Seleccionar el tipo de licencia A
    And Seleccionar el tipo de sangre O+
    And Seleccionar la foto del chofer C:\Users\cesar\OneDrive\Desktop\req\choferFoto.jpg
    Then Aplastar el boton para guardar el chofer
    And Visualizar el chofer guardado

  Scenario: Ingresar un nombre incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón agregar
    And Rellenar el campo Nombre 1234
    And Rellenar el campo Apellido Rios
    And Rellenar el campo Número de Telefono 0999893860
    And Seleccionar el sexo Masculino
    And Rellenar el campo Cédula 1727925602
    And Seleccionar el tipo de licencia A
    And Seleccionar el tipo de sangre O+
    And Seleccionar la foto del chofer C:\Users\cesar\OneDrive\Desktop\req\choferFoto.jpg
    Then Aplastar el boton para guardar el chofer
    And Visualizar el chofer guardado

  Scenario: Ingresar un apellido incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón agregar
    And Rellenar el campo Nombre Pepe
    And Rellenar el campo Apellido 1234
    And Rellenar el campo Número de Telefono 0999893860
    And Seleccionar el sexo Masculino
    And Rellenar el campo Cédula 1727925602
    And Seleccionar el tipo de licencia A
    And Seleccionar el tipo de sangre O+
    And Seleccionar la foto del chofer C:\Users\cesar\OneDrive\Desktop\req\choferFoto.jpg
    Then Aplastar el boton para guardar el chofer
    And Visualizar el chofer guardado

  Scenario: Ingresar un número de teléfono incorrecto
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón agregar
    And Rellenar el campo Nombre Pepe
    And Rellenar el campo Apellido Rios
    And Rellenar el campo Número de Telefono -099989
    And Seleccionar el sexo Masculino
    And Rellenar el campo Cédula 1727925602
    And Seleccionar el tipo de licencia A
    And Seleccionar el tipo de sangre O+
    And Seleccionar la foto del chofer C:\Users\cesar\OneDrive\Desktop\req\choferFoto.jpg
    Then Aplastar el boton para guardar el chofer
    And Visualizar el chofer guardado

  Scenario: Ingresar una cédula incorrecta
    Given Se inicia el navegador
    When Entra a la seccion chofer
    And Aplasta el botón agregar
    And Rellenar el campo Nombre Pepe
    And Rellenar el campo Apellido Rios
    And Rellenar el campo Número de Telefono 0999893860
    And Seleccionar el sexo Masculino
    And Rellenar el campo Cédula 1234567890
    And Seleccionar el tipo de licencia A
    And Seleccionar el tipo de sangre O+
    And Seleccionar la foto del chofer C:\Users\cesar\OneDrive\Desktop\req\choferFoto.jpg
    Then Aplastar el boton para guardar el chofer
    And Visualizar el chofer guardado