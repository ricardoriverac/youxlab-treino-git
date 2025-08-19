package io.github.nicolasgabrielfernandesmm.arquiteturaspring.repository;

import io.github.nicolasgabrielfernandesmm.arquiteturaspring.Entity.EscolaEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EscolaRepository extends JpaRepository<EscolaEntity, Integer> {
}
