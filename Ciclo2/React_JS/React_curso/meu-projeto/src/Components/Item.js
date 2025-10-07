import PropTypes from "prop-types";

function Item({ marca, anoLancamento }) {
  return (
    <>
      <li>
        {marca} - {anoLancamento}
        <p>Teste fragments</p>
      </li>
    </>
  );
}

Item.propTypes = {
  marca: PropTypes.string.isRequired,
  anoLancamento: PropTypes.number,
};
Item.defaultProps = {
    marca: 'Não tem marca',
    anoLancamento: 0,
}

export default Item;
