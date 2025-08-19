import './Form.module.css'

function FormCpf({ type, name, text, value, onChange, onBlur }) {
    return(
        <div>
           <label>{text}</label>
           <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
            maxLength={14}
           />
        </div>
    )
}

export default FormCpf