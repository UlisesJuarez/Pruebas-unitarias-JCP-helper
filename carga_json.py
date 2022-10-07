import requests
lista_preguntas=[
    {
        "enunciado":"¿Qué es un compilador?",
        "autor":"JCP_Helper",
        "tema":"Conceptos basicos",
        "tipo_pregunta":"Abierta",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Traduce lo que escribimos en código fuente a código binario y verifica si hay error en el programa."
    },
    {
        "enunciado":"¿Qué es el código binario?",
        "autor":"JCP_Helper",
        "tema":"Conceptos basicos",
        "tipo_pregunta":"Abierta",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Es el idioma de las computadoras estructurado de 0's y 1's"
    },
    {
        "enunciado":"¿Cuál es la librería principal del lenguaje C?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"math.v,estudio.c,stdio.c,stdio.h",
        "respuesta":"stdio.h"
    },
    {
        "enunciado":"¿Cuál es la función de salida por pantalla del lenguaje c?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"echo,printff(),printf();,scanf()",
        "respuesta":"printf();"
    },
    {
        "enunciado":"¿EL LENGUAJE DE PROGRAMACIÓN ANSI C ES SOLAMENTE DE ALTO NIVEL?",
        "autor":"JCP_Helper",
        "tema":"Conceptos basicos",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"La función return devuelve valores alfanuméricos y caracteres especiales",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"La función scanf lee solo números por teclado",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"¿EL TIPO DE DATO INTEGER SIRVE PARA DECLARAR VALORES ENTEROS EN ANSI C?",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"¿EL TIPO DE DATO FLOAT SIRVE PARA DECLARAR VALORES ENTERO EN ANSI C?",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"¿EN EL LENGUAJE ANSI C CUAL ES EL OPERADOR DE ASIGNACIÓN?",
        "autor":"JCP_Helper",
        "tema":"Operadores",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"%,-,==,=",
        "respuesta":"="
    },
    {
        "enunciado":"¿EN EL LENGUAJE ANSI C CUAL ES EL OPERADOR LÓGICO 'Y'?",
        "autor":"JCP_Helper",
        "tema":"Operadores",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"||,%&,&&,|&",
        "respuesta":"&&"
    },
    {
        "enunciado":"¿EN EL LENGUAJE ANSI C CUAL ES EL OPERADOR LÓGICO 'O'?",
        "autor":"JCP_Helper",
        "tema":"Operadores",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"&&,||,%|,%&",
        "respuesta":"||"
    },
    {
        "enunciado":"¿A=15 y B=7 si la condición if (A>B) cual es el mayor de los dos números?",
        "autor":"JCP_Helper",
        "tema":"Condicionales",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"B,A,BA,AB",
        "respuesta":"A"
    },
    {
        "enunciado":"¿CUAL COMENTARIO ESTA CORRECTO EN ANSI C?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"/* Mi primer programa */,/*// MI primer programa,*// Mi primer programa,/*Mi primer programa /*",
        "respuesta":"/* Mi primer programa */"
    },
    {
        "enunciado":"¿Quien es el creador del lenguaje C?",
        "autor":"JCP_Helper",
        "tema":"Historia",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"Dennis M. Ritchie,James Gosling, Bill Gates,Bjarne Stroustrup",
        "respuesta":"Dennis M. Ritchie"
    },
    {
        "enunciado":"¿Cúal es el caracter utilizado para separar instrucciones?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":";,:,.",
        "respuesta":";"
    },
    {
        "enunciado":"Un programa de C tiene básicamente la siguiente forma: -Comandos del preprocesador. -Definiciones de tipos. -Prototipos de funciones. -Variables Funciones",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"Para declarar una variable en C, se debe seguir el siguiente formato:",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"int a =0;,tipo lista variables;,b=0,0=a",
        "respuesta":"tipo lista variables;"
    },
    {
        "enunciado":"Una variable global puede ser utilizada en cualquier parte del programa",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"""Del siguiente programa cual es el resultado:
#include<stdio.h> 
int main()
{	
    int i;	
    for ( i=0 ; i<5 ; i++ )	
    {
        printf("Hola");	
    }	
}""",
        "autor":"JCP_Helper",
        "tema":"Bucles",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"Hola 0 veces, Hola 100 veces, Hola 5 veces, Hola 1",
        "respuesta":"Hola 5 veces" 
    },
    {
        "enunciado":"""Busca el error en el siguiente programa
#include<stdio.h>  
int main() 
{ 
    int numero; 
    printf( "Introduce un número: " ); 
    scanf( "%d", numero ); 
    printf( "Has introducido el número %d.", numero ); 
    return 0;
}""",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":";,&,&d,Nada le hace falta",
        "respuesta":"&" 
    },
    {
        "enunciado":"""Cual es el fallo del siguiente programa
int main()
{ 
    int a, b, c; 
    a = 5; 
    b = a; 
    c = ( a * b ); 
    
    printf( "%i",c ); 
    getch(); 
}""",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"C",
        "opciones":"nada,declaracion de variables,librerias,las dos anteriores",
        "respuesta":"librerias" 
    },
    {
        "enunciado":"""El siguiente programa compilaria
#include<stdio.h>
#include<stdlib.h>
int main()
{ 
    int a,b,c; 
    a = 5; 
    b = 2; 
    c = a * 2;
    printf( "%i", c ); 
    getch(); 
}""",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en C",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"C",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"¿Cuál es la descripción que crees que define mejor el concepto 'clase' en la programación orientada a objetos?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Es un concepto similar al de 'array',Es un tipo particular de variable,Es un modelo o plantilla a partir de la cual creamos objetos,Es una categoria de datos ordenada secuencialmente",
        "respuesta":"Es un modelo o plantilla a partir de la cual creamos objetos" 
    },
    {
        "enunciado":"¿Qué elementos crees que definen a un objeto?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Su cardinalidad y su tipo,Sus atributos y sus métodos,La forma en que establece comunicación e intercambia mensajes,Su interfaz y los eventos asociado",
        "respuesta":"Sus atributos y sus métodos" 
    },
    {
        "enunciado":"¿Qué código de los siguientes tiene que ver con la herencia?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"public class Componente extends Producto,public class Componente inherit Producto,public class Componente implements Producto,public class Componente belong to Producto",
        "respuesta":"public class Componente extends Producto" 
    },
    {
        "enunciado":"¿Qué significa instanciar una clase?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Duplicar una clase,Eliminar una clase,Crear un objeto a partir de la clase,Conectar dos clases entre sí",
        "respuesta":"Crear un objeto a partir de la clase" 
    },
    {
        "enunciado":"En Java, ¿a qué nos estamos refiriendo si hablamos de 'Swing'?",
        "autor":"JCP_Helper",
        "tema":"Librerias",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Una función utilizada para intercambiar valores,Es el sobrenombre de la versión 1.3 del JDK,Un framework específico para Android,Una librería para construir interfaces gráficas",
        "respuesta":"Una librería para construir interfaces gráficas" 
    },
    {
        "enunciado":"¿Qué es el bytecode en Java?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en Java",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"El formato de intercambio de datos,El formato que obtenemos tras compilar un fuente .java,Un tipo de variable,Un depurador de código",
        "respuesta":"El formato que obtenemos tras compilar un fuente .java" 
    },
    {
        "enunciado":"¿Qué código asociarías a una Interfaz en Java?",
        "autor":"JCP_Helper",
        "tema":"Interfaces",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"public class Componente interface Product,Componente cp = new Componente (interfaz),public class Componente implements Printable,Componente cp = new Componente.interfaz",
        "respuesta":"public class Componente implements Printable" 
    },
    {
        "enunciado":"¿Qué significa sobrecargar (overload) un método?",
        "autor":"JCP_Helper",
        "tema":"Métodos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Editarlo para modificar su comportamiento,Cambiarle el nombre dejándolo con la misma funcionalidad,Crear un método con el mismo nombre pero diferentes argumentos,Añadirle funcionalidades a un método",
        "respuesta":"Crear un método con el mismo nombre pero diferentes argumentos" 
    },
    {
        "enunciado":"¿Qué es una excepción?",
        "autor":"JCP_Helper",
        "tema":"Excepciones",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Un error que lanza un método cuando algo va mal,Un objeto que no puede ser instanciado,Un bucle que no finaliza,Un tipo de evento muy utilizado al crear interfaces",
        "respuesta":"Un error que lanza un método cuando algo va mal" 
    },
    {
        "enunciado":"Algunas palabras de palabras claves de java",
        "autor":"JCP_Helper",
        "tema":"Palabras reservadas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Booleanos true false,cast future generic,abstract continue for Boolean default goto null,Interface Implements Public Extends",
        "respuesta":"abstract continue for Boolean default goto null" 
    },
    {
        "enunciado":"Cual de estas son palabras reservadas de java",
        "autor":"JCP_Helper",
        "tema":"Palabras reservadas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"cast future generic,continue for Boolean,default goto null,Implements Public Extends",
        "respuesta":"cast future generic" 
    },
    {
        "enunciado":"Cual de estos son operadores de java",
        "autor":"JCP_Helper",
        "tema":"Operadores",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"*=/,() . ;,%/,/** * /",
        "respuesta":"*=/" 
    },
    {
        "enunciado":"¿Qué es objeto en java?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Es un conjunto de declaraciones de funciones,Es una agrupación que termina una cadena de herencia,Es una agrupación de datos y de funciones,Es conjunto de variables y funciones relacionadas con esas variables",
        "respuesta":"Es conjunto de variables y funciones relacionadas con esas variables" 
    },
    {
        "enunciado":"¿Cuáles son las variables de objeto en java?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Es un conjunto de declaraciones de funciones,Encapsulamiento y herencia,Es una agrupación de datos y de funciones,Implements Public Extends",
        "respuesta":"Encapsulamiento y herencia" 
    },
    {
        "enunciado":"¿Qué es una clase en java?",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Es un conjunto de declaraciones de funciones,Es una agrupación que termina una cadena de herencia,Es una agrupación de datos y de funciones,Es conjunto de variables y funciones relacionadas con esas variables",
        "respuesta":"Es una agrupación de datos y de funciones" 
    },
    {
        "enunciado":"A los menos cuantos métodos tiene una clase abstract",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"5,2,1,28",
        "respuesta":"1" 
    },
    {
        "enunciado":"Para que se utiliza la clase abstract",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Para poder ser accesibles en otras clases,Para acceder desde otros paquetes,Para la clase base para la herencia,Para ser una súper clase",
        "respuesta":"Para la clase base para la herencia" 
    },
    {
        "enunciado":"Cómo se declara una clase final",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"como la clase que termina una cadena de herencia,simulando la herencia múltiple,mediante la palabra clase implements,al especificar mediante la palabra clave extends",
        "respuesta":"como la clase que termina una cadena de herencia" 
    },
    {
        "enunciado":"¿Cómo deben estar las clases public para acceder a ellas desde otras clases?",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Declaradas,Importadas,Directas, Por herencia",
        "respuesta":"Importadas" 
    },
    {
        "enunciado":"¿Cómo se llama la clase que termina una cadena de herencia?",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Public, Abstract, final",
        "respuesta":"final" 
    },
    {
        "enunciado":"¿Cómo se especifica las clases que tiene una súper clase?",
        "autor":"JCP_Helper",
        "tema":"Clases",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Implements,Interface,Extends,Object",
        "respuesta":"Extends" 
    },
    {
        "enunciado":"Si no se especifica una súper clase se asume que se hereda de la clase",
        "autor":"JCP_Helper",
        "tema":"Herencia",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Objects,Extends,Implements,Interface",
        "respuesta":"Interface" 
    },
    {
        "enunciado":"¿Qué es una interface?",
        "autor":"JCP_Helper",
        "tema":"Interfaces",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Una súper clase,Es un conjunto de declaraciones de funciones,Una herencia múltiple,Un fichero public",
        "respuesta":"Es un conjunto de declaraciones de funciones" 
    },
    {
        "enunciado":"¿Cómo se debe llamar el fichero con extensión .java?",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en Java",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"El fichero se debe llamar como atributo,El fichero se debe llamar como la clase interface,El fichero se debe llamar como la clase object,El fichero de debe llamar como la clase public",
        "respuesta":"El fichero de debe llamar como la clase public" 
    },
    {
        "enunciado":"Menciona los tres modificadores de acceso",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en Java",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Java",
        "opciones":"Static-final-private,clase-static-public,public-private-protected,class-final-static",
        "respuesta":"public-private-protected" 
    },
    {
        "enunciado":"¿Qué es Encapsulamiento? Es la Habilidad del programador para ocultar datos",
        "autor":"JCP_Helper",
        "tema":"Encapsulamiento",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Java",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"¿Qué es herencia? Es una Relación entre las clases en las que las clases comparten la estructura y el comportamiento de la clase padre",
        "autor":"JCP_Helper",
        "tema":"Herencia",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Java",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"Qué es polimorfismo? es cuando un objeto se puede comportar de muchas formas o un método puede comportarse de muchas formas",
        "autor":"JCP_Helper",
        "tema":"Polimorfismo",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Java",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"¿Se admite la herencia múltiple en Java?",
        "autor":"JCP_Helper",
        "tema":"Herencia",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Java",
        "opciones":"",
        "respuesta":"Falso" 
    },
    {
        "enunciado":"¿Elementos que define un objeto son: Atributos y métodos?",
        "autor":"JCP_Helper",
        "tema":"POO",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Java",
        "opciones":"",
        "respuesta":"Verdadero" 
    },
    {
        "enunciado":"""Si ejecutamos, el siguiente código cuál seria su salida:
>>>a=1
>>>print(a+b)
""",
        "autor":"JCP_Helper",
        "tema":"Estructura básica de un programa en python",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"'b' is not defined,1,a+b,NaN",
        "respuesta":"'b' is not defined"
    },
    {
        "enunciado":"""if('1'='1'): 
    print('1')
En las lineas de código que falta para que funcione:""",
        "autor":"JCP_Helper",
        "tema":"Operadores",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"=,Nada,Mal identado,;",
        "respuesta":"="
    },
    {
        "enunciado":"""a='Examen'
print(a[6])

¿Cual seria su salida?""",
        "autor":"JCP_Helper",
        "tema":"Tipo de datos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"name 'a' is not defined,string index out of range,N,n",
        "respuesta":"string index out of range"
    },
    {
        "enunciado":"""a='Examen'
print(a[2])

¿Cuál seria su salida?""",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"name 'a' is not defined,string index out of range,a,x",
        "respuesta":"a"
    },
    {
        "enunciado":"""def valor(x): 
    return x+x
print(valor(1))

¿Cuál seria su salida?""",
        "autor":"JCP_Helper",
        "tema":"Funciones",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"2,4,x,1",
        "respuesta":"2"
    },
    {
        "enunciado":"Un objeto de tipo Int (Número entero) es ________. (Mutable / Inmutable)",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Rellenar espacios",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"inmutable"
    },
    {
        "enunciado":"¿Cuál de estos tipos de datos es mutable?",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"bool (Booleano),decimal,float (Número de coma flotante),Ninguno de los anteriores",
        "respuesta":"Ninguno de los anteriores"
    },
    {
        "enunciado":"Los strings en Python son inmutables",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"Las listas son mutables",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"¿Cuál de estos tipos de datos es inmutable?",
        "autor":"JCP_Helper",
        "tema":"Tipos de datos",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"diccionarios,bytearrays,sets,ninguno de los anteriores",
        "respuesta":"ninguno de los anteriores"
    },
    {
        "enunciado":"Se crean utilizando paréntesis",
        "autor":"JCP_Helper",
        "tema":"Tuplas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"listas,tuplas,listas y tuplas, ninguna de las anteriores",
        "respuesta":"tuplas"
    },
    {
        "enunciado":"Se crean usando corchetes",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"listas,tuplas,listas y tuplas,ninguna de las anteriores",
        "respuesta":"listas"
    },
    {
        "enunciado":"""El siguiente error se genera al intentar modificar el contenido de una tupla.
TypeError: 'xxxxx' object does not support item assignment
""",
        "autor":"JCP_Helper",
        "tema":"Tuplas",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"El metodo .append() es utilizado en las tuplas",
        "autor":"JCP_Helper",
        "tema":"Tuplas",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Falso"
    },
    {
        "enunciado":"Las tuplas suelen contener una secuencia heterogénea de elementos",
        "autor":"JCP_Helper",
        "tema":"Tuplas",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"Las listas suelen contener una secuencias homogénea de elementos",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Verdadero o Falso",
        "lenguaje":"Python",
        "opciones":"",
        "respuesta":"Verdadero"
    },
    {
        "enunciado":"""¿Cuál de las opciones nos permite obtener una lista con los siguientes valores : [9,16,25]?

lst_num = [3,4,5]
""",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"output = [n * 2 for n in lst_num],output = [n ** 2 for n in lst_num],output = [n ** 2 for lst_num in n],output = [n ^2 for n in lst_num]",
        "respuesta":"output = [n ** 2 for n in lst_num]"
    },
    {
        "enunciado":"""Completa la linea de código faltante para obtener los textos en mayúscula a partir de la siguiente lista:

lst_lp = ["python", "c", "java","php"]
""",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"output = [lp.upper() for lp in lst_lp],output = [lp.capitalize() for lp in lst_lp],output = [lp.lower() for lp in lst_lp],output = [lp.uppercase() for lp in lst_lp]",
        "respuesta":"output = [lp.upper() for lp in lst_lp]"
    },
    {
        "enunciado":"""¿Cuál de las opciones nos permite obtener una lista con los siguientes elementos: [2, 3, 3, 4]?

lst_num = [1, 2, 3, 4]
""",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"output = [n + 1 if n < 4 else n for n in lst_num],output = [n + 1 if n < 2 else n for n in lst_num],output = [n + 1 if n <= 3 else n for n in lst_num],output = [n + 1 if n <= 2 else n for n in lst_num]",
        "respuesta":"output = [n + 1 if n <= 2 else n for n in lst_num]"
    },
    {
        "enunciado":"""¿Cuál de las opciones nos permite obtener una lista con los siguientes elementos: ['P', 'P', ‘H’]?.

letras_1 = ['P','Y','T', 'H','O', 'N']
letras_2 = ['P','H','P']
""",
        "autor":"JCP_Helper",
        "tema":"Listas",
        "tipo_pregunta":"Opción multiple",
        "lenguaje":"Python",
        "opciones":"output = [a for a in letras_1 for b in letras_2 if a = b],output = [a if a == b for a in letras_1 for b in letras_2],output = [a for a in letras_1 for b in letras_2 if a == b],",
        "respuesta":"output = [a for a in letras_2 for b in letras_1 if a = b]"
    }
]

#Tipos de preguntas
#Opción multiple
#Verdadero o Falso
#Abierta
#Rellenar espacios

url="http://127.0.0.1:5000/nueva_pregunta?"

for item in lista_preguntas:
    response=requests.request("POST",url=url,params=item)
    print(response.text)


