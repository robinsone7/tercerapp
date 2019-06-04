import React from 'react';

const AddUser = (props) => {
    return(
        <form>
            <div className="field">
              <input
              name="username"
              className="input is-large"
              type="text"
              placeholder="Ingrese un nombre de usuario"
              />
            </div>
            <div className="field">
              <input
              name="email"
              className="input is-large"
              type="email"
              placeholder="Ingrese una direccion email"
              />
            </div>
           
              <input
              type="submit"
              className="button is-link is-fullwidth"
              value="Enviar"
              
              />
           

        </form>
    )
};

export default AddUser;
    
