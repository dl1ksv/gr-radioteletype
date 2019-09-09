/* -*- c++ -*- */
/*
 * Copyright 2019 dl1ksv.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef _QA_ASYNC_WORD_EXTRACTOR_BB_H_
#define _QA_ASYNC_WORD_EXTRACTOR_BB_H_

#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestCase.h>

namespace gr {
  namespace radioteletype {

    class qa_async_word_extractor_bb : public CppUnit::TestCase
    {
    public:
      CPPUNIT_TEST_SUITE(qa_async_word_extractor_bb);
      CPPUNIT_TEST(t1);
      CPPUNIT_TEST_SUITE_END();

    private:
      void t1();
    };

  } /* namespace radioteletype */
} /* namespace gr */

#endif /* _QA_ASYNC_WORD_EXTRACTOR_BB_H_ */

