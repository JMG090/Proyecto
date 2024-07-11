# project/ising.py

"""Este módulo contiene las funciones que fueron utilizadas para evaluar la dinámica del modelo de Ising.

El módulo contiene las siguientes funciones:

- `hamiltonian(J, g, N)` - Devuelve la matriz del hamiltoniano del modelo de Ising y un arreglo de las matrices $\hat{\sigma}^z_{i}$.
- `schrodinger(ham, psi)` - Devuelve la ecuación de Schrödinger.
- `rk4(func, ham, y_n, h)` - Devuelve el siguiente estado cuántico partiendo de un estado inicial.

"""

def hamiltonian(J, g, N):
    """Construye el hamiltoniano del modelo de Ising cuántico de ferromagnetismo en una dimensión con condicones de frontera periódicas.

    Examples:
        >>> hamiltonian(2.0, 1.0, 2)
        (array([[ 4.+0.j,  1.+0.j,  1.+0.j,  0.+0.j], [ 1.+0.j, -4.+0.j,  0.+0.j,  1.+0.j], [ 1.+0.j,  0.+0.j, -4.+0.j,  1.+0.j], [ 0.+0.j,  1.+0.j,  1.+0.j,  4.+0.j]]), [array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j], [ 0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j], [ 0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j], [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]]), array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j], [ 0.+0.j, -1.+0.j,  0.+0.j,  0.+0.j], [ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j], [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])])


    Args: 
       J (float): Parámetro de interacción ferromagnética entre espines.
       g (float): Parámetro del campo magnético exterior.
       N (int): Número de espines.


    Returns:
       (tuple): El primer elemento contiene la matriz calculada del Hamiltoniano. El segundo contiene las matrices $\hat{\sigma}^z_{i}$ para cada espín utilizadas en la construcción del Hamiltoniano.  

    """

    sigma_z = [0] * N
    sigma_x = [0] * N

    for i in range(N):

        sigma_zi = [0] * N
        sigma_xi = [0] * N  

        for j in range(i):

            sigma_zi[j] = (iden)
            sigma_xi[j] = (iden)

        sigma_zi[i] = (sz)  
        sigma_xi[i] = (sx)

        for k in range(i+1,N):

            sigma_zi[k] = (iden) 
            sigma_xi[k] = (iden)

        sigma_z[i] = (qt.tensor(sigma_zi)).full()
        sigma_x[i] = (qt.tensor(sigma_xi)).full()


    h_first = 0.0  
    h_second = 0.0 

    for i in range(N): 

        h_first += J*np.dot(sigma_z[i], sigma_z[(i+1)%N])

    for i in range(N):

        h_second += g*np.array(sigma_x[i])


    return (h_first + h_second), sigma_z




def schrodinger(ham, psi):
    """Construye la forma de la ecuación de Schrödinger
    
    Examples: 
        >>> H = np.array([[4, 1, 1, 0],[1, -4, 0, 1],[1, 0, -4, 1],[0, 1, 1, 4]], dtype=np.complex128)
        >>> psi = np.array([0.0, 1.0, 0.0, 0.0])
        >>> schrodinger(H, psi)
        [0.-1.j 0.+4.j 0.-0.j 0.-1.j]

    Args:
        ham (array): Hamiltoniano del sistema cuántico.
        psi (array): Estado cuántico del sistema.

    Returns: 
        (ndarray): Aplicación del operador Hamiltoniano al estado cuántico multiplicado por el imaginario -i.

    """
    return -1.0j*(np.dot(ham, psi))




def rk4(func, ham, y_n, h):
    """Implementa el método de Runge-Kutta de 4to orden.
    
    Examples:
        >>> H = np.array([[4, 1, 1, 0],[1, -4, 0, 1],[1, 0, -4, 1],[0, 1, 1, 4]], dtype=np.complex128)
        >>> psi = np.array([0.0, 1.0, 0.0, 0.0])
        >>> def schrodinger(ham, psi): return -1.0j*(np.dot(ham, psi))
        >>> rk4(schrodinger, H, psi, 1)
        [0. +2.33333333j 5.66666667-8.j 2. -1.33333333j 0. +2.33333333j]

    Args: 
        func (function): Función a evaluar.
        ham (array): Hamiltoniano del sistema cuántico.
        y_n (array): Estado cuántico actual del sistema.
        h (float): Paso de tiempo.

    Returns: 
        (array): Siguiente estado cuántico del sistema. 

    """
    k_1 = func(ham ,y_n)

    k_2 = func(ham ,y_n + (h/2) * k_1)

    k_3 = func(ham ,y_n + (h/2) * k_2)

    k_4 = func(ham ,y_n + h * k_3)

    return y_n + (h/6)*(k_1+2*k_2+2*k_3+k_4)





