import './Form.module.css'

function Form({ type, name, text, value, onChange }) {
    return(
        <div>
           <label>{text}</label>
           <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
           />
        </div>
    )
}

export default Form
