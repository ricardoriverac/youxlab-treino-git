import styles from "./Input.module.css";

function Input({ text, name, type, placeholder }) {
  return (
    <div className={styles.form_control}>
      <label htmlFor={name}> {text}: </label>
      <input 
        type={type}
        name={name}
        id={name}
        placeholder={placeholder}
      />
    </div>
  );
}
export default Input;
