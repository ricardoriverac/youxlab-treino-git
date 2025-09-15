import styles from "./Select.module.css";

function Select({
  type,
  text,
  option,
  name,
  placeholder,
  handleOnchange,
  value,
}) {
  return (
    <div className={styles.form_control}>
      <label htmlFor={name}>{text}:</label>
      <select name={name} id={name} />
      <option>Selecione uma opção</option>
    </div>
  );
}

export default Select;
