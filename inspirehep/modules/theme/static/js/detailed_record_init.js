/*
 * This file is part of INSPIRE.
 * Copyright (C) 2015 CERN.
 *
 * INSPIRE is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * INSPIRE is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
 *
 * In applying this licence, CERN does not waive the privileges and immunities
 * granted to it by virtue of its status as an Intergovernmental Organization
 * or submit itself to any jurisdiction.
 */

require([
  "js/plots",
  "js/datatables",
  "impact-graphs",
  'angular-loading-bar',
  'invenio-search',
  'inspirehep-search'
], function(Plots) {
  angular.element(document).ready(function() {
    angular.bootstrap(
      document.getElementById("record_content"), ['angular-loading-bar',
                                                  'inspirehepSearch']
    );
  });
	console.log('js/detailed_record_init is loaded')
});
