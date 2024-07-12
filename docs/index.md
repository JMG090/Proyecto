# Modelo de Ising cuántico unidimensional en una grilla de N espines: Dinámica de muchos cuerpos

$\textbf{Coordinador:}$ Marlon Brenes Navarro

$\textbf{Estudiantes:}$
 
* C02637 Andrés Díaz Pereira 
* C24634 Felipe Mata
* C05127 Julyana Mora García 
* 890465 Patricio Becerra Barrios 
* C27118 Sebastián José Salazar Chaves

## Modelo de Ising

El modelo de Ising para el estudio de la transición ferromagnética es de gran interés debido a su sencillez y que se puede resolver analíticamente. Su hamiltoniano está dado por:
\begin{equation}
\hat{H} = \sum_{i=1}^{N-1} J\hat{\sigma}^z_{i} \hat{\sigma}^z_{i+1} + \sum_{i=1}^N g\hat{\sigma}^x_{i},
\end{equation}

El primer término representa la energía de interacción entre los espines contiguos $\textit{i}$ y $\textit{i+1}$ donde $\textit{J}$ es una escala energética que determina la interacción ferromagnética. El segundo término es la energía de interacción entre los momentos magnéticos y un campo magnético externo, $\textit{g}$ es el parámetro energético del campo trasversal. Los términos $\hat{\sigma}^\alpha_{i}$ donde $\alpha = x,y,z$ son las matrices de Pauli para el espín $\textit{i}$

La construcción del Hamiltoniano implica crear una matriz hermítica de dimensión $2^N$ que describe el sistema. Para ello se utilizan productos tensoriales de cada uno de los espacios de Hilbert de la forma:
\begin{equation}
\hat{\sigma}^\alpha_{1} = \hat{\sigma}^z \otimes \mathbb{1} \otimes \mathbb{1} \otimes \cdots \otimes  \mathbb{1} \otimes \mathbb{1} \otimes \mathbb{1}, 
\end{equation}
\begin{equation}
\hat{\sigma}^\alpha_{N-1} = \mathbb{1} \otimes \mathbb{1} \otimes \mathbb{1} \otimes \cdots \otimes  \mathbb{1} \otimes \hat{\sigma}^z \otimes \mathbb{1},
\end{equation}
\begin{equation}
\hat{\sigma}^\alpha_{N} = \mathbb{1} \otimes \mathbb{1} \otimes \mathbb{1} \otimes \cdots \otimes  \mathbb{1} \otimes \mathbb{1} \otimes \hat{\sigma}^z 
\end{equation} 

realizando así $N-1$ productos tensoriales para calcular cada $\hat{\sigma}^\alpha_{i}$ 

La dinámica de un estado puro se describe mediante la $\textit{ecuación de Schrödinger}$, la cuál está dada por:
\begin{equation}
\frac{d{\psi}(t)}{dt} = -{\rm{i}} \hat{H}|\psi(t) \rangle,
\end{equation}

cuya solución analítica está dada por:
\begin{equation}
\psi(t) = e^{-{\rm{i}}\hat{H}(t-t_{0})} |\psi(t=t_{0}) \rangle,
\end{equation}

Por lo tanto, la solución involucra resolver de manera numérica la ecuación diferencial de Schrödinger o evaluar de alguna forma la exponencial de la matriz.

## Project Overview

::: project
