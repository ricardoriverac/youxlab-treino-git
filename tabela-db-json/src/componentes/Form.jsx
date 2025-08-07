import './Form.module.css'

function Form({ type, name, text, value, onChange, onBlur }) {
    return(
        <div>
           <label>{text}</label>
           <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
            onBlur={onBlur}
           />
        </div>
    )
}

export default Form
